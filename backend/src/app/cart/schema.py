import typing as t
import uuid
import pydantic as pyd
from src.app.product import schema as product_schema


class ICartIn(pyd.BaseModel):
    pdf: t.Optional[bool] = True
    paper_back_qty: t.Optional[int] = 0
    hard_back_qty: t.Optional[int] = 0
    product_id: uuid.UUID


class ICartOut(pyd.BaseModel):
    id: uuid.UUID
    pdf: t.Optional[bool] = True
    paper_back_qty: t.Optional[int] = 0
    hard_back_qty: t.Optional[int] = 0
    product: product_schema.IProductShortInfo

    class Config:
        orm_mode = True
