import typing as t
from app.src._base.schemas import Message
from app.src.order.enum import OrderStatus
from app.src.payment.models import Payment
from app.src.payment.schemas import PaymentResponse, PaymentLinkData, PaymentMeta, PaymentVerifyOut, VerifyPaymentResponse
from app.src.user.models import User
from fastapi import HTTPException, status
from app.src.order.models import Order, OrderItem
from app.utils.payments import generate_link, get_product_total_price, verify_payment
from app.core.config import settings


async def create_payment(orderId: str, user: User):
    get_order: Order = await Order.objects.get_or_none(orderId=orderId)
    if not get_order:
        raise HTTPException(
            detail=f"order with Id {orderId} not found", status_code=status.HTTP_404_NOT_FOUND)
    order_items: t.List[OrderItem] = await OrderItem.objects.select_related("product__property").filter(order=get_order).all()
    if not order_items:
        raise HTTPException(detail="order items can not be empty")
    total_price = get_product_total_price(order_items)
    if total_price > 0:
        meta_data: PaymentMeta = PaymentMeta(order_id=get_order.orderId,
                                             user_id=user.id,
                                             cancel_action=f"{settings.PROJECT_URL}")
        payment_data: PaymentLinkData = PaymentLinkData(
            amount=total_price,
            email=user.email,
            metadata=meta_data.dict(),
            callback_url=f"{settings.PROJECT_URL}/payment"
        )
    data_out: PaymentResponse = generate_link(dataIn=payment_data)
    if data_out.data.authorization_url:
        return data_out
    raise HTTPException(detail="error creating payment link",
                        status_code=status.HTTP_201_CREATED)


async def verify_user_payment(data: VerifyPaymentResponse, user: User):
    check_payment: PaymentVerifyOut = verify_payment(reference=data.reference)
    if check_payment.data.status == "success":
        get_order = await Order.objects.get_or_none(orderId=data.orderId, user=user)
        if not get_order:
            raise HTTPException(
                detail=f"order with id {data.orderId} does not exist", status_code=status.HTTP_404_NOT_FOUND)
        save_payment = await Payment.objects.create(
            pay_ref=check_payment.data.reference,
            user=user,
            order=get_order,
            amount=check_payment.data.amount,
            currency=check_payment.data.currency.lower(),
            method=check_payment.data.channel,
            status=check_payment.data.status
        )
        if save_payment:
            get_order.status = OrderStatus.COMPLETED
            await get_order.upsert()
            return Message(message="payment successful")
        raise HTTPException(detail="internal server error",
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
