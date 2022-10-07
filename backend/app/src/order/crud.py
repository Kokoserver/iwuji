import typing as t
from fastapi import status, HTTPException
from app.src._base.schemas import Message
from app.src.address.models import ShippingAddress
from app.src.cart.models import Cart
from app.src.order.models import Order, OrderItem
from app.src.order.enum import OrderStatus
from app.src.order.schemas import OrderIn
from app.src.user.models import User
from starlette.responses import Response


def check_quantity(carts: t.List[Cart])->t.List[str]:
    error_list: t.List[str] = []
    for cart in carts:
        if cart.hard_back_qty > cart.product.property.hard_back_qty:
            error_list.append(
                f"only {cart.product.property.hard_back_qty} left of {cart.product.name}"
            )
        if cart.paper_back_qty > cart.product.property.paper_back_qty:
            error_list.append(
                f"only {cart.product.property.hard_back_qty} left of {cart.product.name}"
            )
    return error_list


async def create_order(data: OrderIn, user: User)->dict:
    get_shipping_address = await ShippingAddress.objects.get_or_none(id=data.addressId, user=user)
    if not get_shipping_address:
        raise HTTPException(detail="Shipping address does not exist",
                            status_code=status.HTTP_404_NOT_FOUND)
    get_cart_product = await Cart.objects.select_related("product__property").filter(user=user).all()
    if not get_cart_product:
        raise HTTPException(detail="User cart is empty",
                            status_code=status.HTTP_400_BAD_REQUEST)
    check_product_qty = check_quantity(get_cart_product)
    if len(check_product_qty) > 0:
        raise HTTPException(detail=check_product_qty,
                            status_code=status.HTTP_400_BAD_REQUEST)
    create_order = await Order.objects.create(user=user,
                                              shipping_address=get_shipping_address,
                                              status=OrderStatus.PROCESSING
                                              )

    if create_order:
        order_items = [OrderItem(pdf=cart.pdf,
                                 paper_back_qty=cart.paper_back_qty,
                                 hard_back_qty=cart.hard_back_qty,
                                 product=cart.product,
                                 order=create_order
                                 )
                       for cart in get_cart_product if get_cart_product
                       ]
        await OrderItem.objects.bulk_create(order_items)
        await Cart.objects.filter(user=user).delete()
        return {"orderId": create_order.orderId}


async def get_all_orders(user: User, offset: int = 0, limit: int= 10, filter: str='')->t.List[Order]:
    all_order = await Order.objects.filter(status=filter, user=user).limit(limit).offset(offset).all()
    return all_order


async def get_order(user: User, orderId: str)->Order:
    order = await Order.objects.get_or_none(orderId=orderId, user=user)
    if order:
        return order
    raise HTTPException(
        detail=f"order with id {orderId} not found", status_code=status.HTTP_404_NOT_FOUND)


async def delete_order(user: User, orderId: str)->None:
    check_order = await Order.objects.get_or_none(orderId=orderId, user=user)
    if check_order:
        await check_order.delete()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
