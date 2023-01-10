from typing import Optional
from backend.src.media.schemas import MediaBase
from pydantic import BaseModel
from pydantic.types import condecimal


class CartIn(BaseModel):
    productId: int
    pdf: bool
    paper_back_qty: int
    hard_back_qty: int


class CartUpdateIn(BaseModel):
    cartId: int
    pdf: bool
    paper_back_qty: int
    hard_back_qty: int


class CartProductPropertyOut(BaseModel):
    hard_back_price: condecimal(max_digits=10, decimal_places=2)
    paper_back_price: condecimal(max_digits=10, decimal_places=2)
    pdf_price: condecimal(max_digits=10, decimal_places=2)


class CartProductOut(BaseModel):
    name: str
    cover_img: Optional[MediaBase]
    property: CartProductPropertyOut


class CartOut(BaseModel):
    id: int
    pdf: bool
    paper_back_qty: int
    hard_back_qty: int
    product: CartProductOut
