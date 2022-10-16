import typing as t
from app.src._base.schemas import Message
from app.src.order.enum import OrderStatus
from .enum import PaymentStatus
from app.src.payment.models import Payment
from app.src.payment.schemas import (
    Customer,
    PaymentResponse,
    PaymentLinkData,
    PaymentMeta,
    PaymentVerifyOut,
    VerifyPaymentResponse,
    PaymentIn,
    PaymentInitOut,
)
from app.src.user.models import User
from fastapi import HTTPException, status
from app.src.order.models import Order, OrderItem
from app.utils.payments import generate_link, get_product_total_price, verify_payment
from app.core.config import settings


async def create_payment(orderIn: PaymentIn, user: User):
    get_order: Order = await Order.objects.get_or_none(orderId=orderIn.orderId)

    if not get_order:
        raise HTTPException(
            detail=f"order with Id {orderIn.orderId} not found",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    order_items: t.List[OrderItem] = (
        await OrderItem.objects.select_related("product__property")
        .filter(order=get_order)
        .all()
    )
    if not order_items:
        raise HTTPException(
            detail="order items can not be empty", status_code=status.HTTP_404_NOT_FOUND
        )
    total_price = get_product_total_price(order_items)
    if total_price > 0:
        await Payment.objects.create(
            pay_ref=get_order.orderId,
            user=user,
            order=get_order,
            amount=total_price,
        )

        meta_data: PaymentMeta = PaymentMeta(
            order_id=get_order.orderId, user_id=user.id
        )
        customer = Customer(
            email=user.email,
            name=f"{user.firstname} {user.lastname}",
            user_id=user.id,
            order_id=get_order.id,
        )
        payment_data: PaymentLinkData = PaymentLinkData(
            tx_ref=get_order.orderId,
            amount=total_price,
            meta=meta_data.dict(),
            customer=customer.dict(),
            redirect_url=f"{settings.PROJECT_URL}/dashboard/payment/{user.firstname}",
        )
        data_out: PaymentResponse = generate_link(dataIn=payment_data)
        if data_out.status == "success":
            return PaymentInitOut(paymentLink=data_out.data.link)
    raise HTTPException(
        detail="error creating payment link",
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


async def payment_list(user: User):
    return await Payment.objects.filter(user=user).order_by('-id').limit(10).all()


async def verify_user_payment(data: VerifyPaymentResponse, user: User):
    get_payment = await Payment.objects.get_or_none(pay_ref=data.tx_ref, user=user)
    if not get_payment:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="invalid payment details was provided",
        )
    try:
        check_payment: PaymentVerifyOut = verify_payment(tx_ref=data.tx_ref)
        if not check_payment.error:
            get_order = await Order.objects.get_or_none(
                orderId=data.tx_ref,
                user=user,
            )
            if not get_order:
                raise HTTPException(
                    detail=f"order with id {data.tx_ref} does not exist",
                    status_code=status.HTTP_404_NOT_FOUND,
                )
            if get_order.orderId != get_payment.pay_ref:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Error validating payment details",
                )
            if get_payment.amount != check_payment.amount:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Error validating payment details",
                )

            await get_payment.update(status=PaymentStatus.SUCCESS)
            await get_order.update(status=OrderStatus.PROCESSING)
            return Message(message="payment successful")
    except:
        await get_payment.update(status=PaymentStatus.FAIL)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="verification failed",
        )
    raise HTTPException(
        status_code=status.HTTP_402_PAYMENT_REQUIRED, detail="payment failed"
    )
