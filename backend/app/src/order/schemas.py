
from pydantic import BaseModel


class OrderItemsIn(BaseModel):
    pdf: bool
    paper_back_qty: int
    hard_back_qty: int
    product: int
    order: int


class OrderIn(BaseModel):
    addressId: int


class OrderOut(BaseModel):
    orderId: str
