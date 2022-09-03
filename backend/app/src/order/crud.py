import typing as t
import requests
from fastapi import status, HTTPException
from app.src.address.models import ShippingAddress
from app.src.cart.models import Cart
from app.src.order.models import Order, OrderItem
from app.src.order.enum import OrderStatus
from app.src.order.schemas import OrderIn
from app.src.user.models import User


def get_product_total_price(carts: t.List[Cart]):
    if carts:
        pdf_price = 0
        hard_back_price = 0
        paper_back_price = 0
        for cart in carts:
            if cart.pdf:
                pdf_price += cart.product.property.pdf_price
            hard_back_price += cart.hard_back_qty * cart.product.property.hard_back_price
            paper_back_price += cart.paper_back_qty * cart.product.property.paper_back_price
        total_price = pdf_price + hard_back_price + paper_back_price
        return total_price


def check_quantity(carts: t.List[Cart])->t.List[str]:
    error_list: t.List[str] = []
    for cart in carts:
        if cart.hard_back_qty < cart.product.property.hard_back_qty:
            error_list.append(
                f"only {cart.product.property.hard_back_qty} left of {cart.product.name}"
            )


async def create_order(data: OrderIn, user: User):
    get_shipping_address = await ShippingAddress.objects.get_or_none(id=data.addressId, user=user)
    if not get_shipping_address:
        raise HTTPException(detail="Shipping address does not exist",
                            status_code=status.HTTP_404_NOT_FOUND)
    get_cart_product = await Cart.objects.select_related("product__property").filter(user=user).all()
    if not get_cart_product:
        raise HTTPException(detail="User cart is empty",status_code=status.HTTP_400_BAD_REQUEST)
    check_product_qty = check_quantity(get_cart_product)
    if len(check_product_qty) > 0:
        raise HTTPException(detail=check_product_qty,status_code=status.HTTP_400_BAD_REQUEST)
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
        new_order_items = await OrderItem.objects.bulk_create(order_items)
        total_price: int = get_product_total_price(get_cart_product)
        if total_price > 0 and new_order_items:
            await Cart.objects.select_related("product").filter(user=user).delete()
            
            

        # generate payment link
