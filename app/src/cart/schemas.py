from uuid import UUID
from pydantic import BaseModel

class CartIn(BaseModel):
    productId: UUID
    pdf: bool
    paper_back_qty: int
    hard_back_qty: int
   
   
class CartOut(BaseModel):
    id: UUID
    pdf: bool
    paper_back_qty: int
    hard_back_qty: int
    created_at: str
    updated_at: str
    