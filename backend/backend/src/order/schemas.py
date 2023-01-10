
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from backend.src.address.schemas import AddressOut

from backend.src.order.enum import OrderStatus
from backend.src.payment.schemas import PaymentDataViewOut
from backend.src.product.schemas import OrderProductOut


class OrderItemsIn(BaseModel):
    pdf: bool
    paper_back_qty: int
    hard_back_qty: int
    product: int
    order: int


class OrderListOut(BaseModel):
    orderId: str
    status: OrderStatus


class OrderProduct(BaseModel):
    id: int
    pdf: bool
    deliver: bool
    paper_back_qty: int
    hard_back_qty: int
    product: OrderProductOut


class OrderDetailsOut(BaseModel):
    id: int
    orderId: str
    status: OrderStatus
    shipping_address: AddressOut
    order_payment: Optional[List[PaymentDataViewOut]]
    order_item_order: List[OrderProduct]
    created_at: datetime


class OrderIn(BaseModel):
    addressId: int


class OrderOut(BaseModel):
    orderId: str
