from datetime import datetime
from pydantic import BaseModel, Field


class ReviewIn(BaseModel):
    comment: str = Field(None, max_length=250)
    rating:int = Field(..., ge=0, lt=11)
    productId:int = None

    
class ReviewOut(BaseModel):
    id:int 
    created_at: datetime
    