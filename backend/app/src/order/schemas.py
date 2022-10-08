
from pydantic import BaseModel

from app.src.order.enum import OrderStatus


class OrderItemsIn(BaseModel):
    pdf: bool
    paper_back_qty: int
    hard_back_qty: int
    product: int
    order: int

class OrderDetailsOut(BaseModel):
    orderId:str
    status:OrderStatus

class OrderIn(BaseModel):
    addressId: int


class OrderOut(BaseModel):
    orderId: str
