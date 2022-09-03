
from pydantic import BaseModel


class OrderIn(BaseModel):
    addressId: int


class OrderOut(BaseModel):
    link: str
