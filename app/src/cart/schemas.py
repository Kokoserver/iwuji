from pydantic import BaseModel


class CartIn(BaseModel):
    productId:int
    pdf: bool
    paper_back_qty: int
    hard_back_qty: int
   
   
class CartOut(BaseModel):
    id:int
    pdf: bool
    paper_back_qty: int
    hard_back_qty: int
    created_at: str
    updated_at: str
    
