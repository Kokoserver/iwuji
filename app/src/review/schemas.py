

from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field


class ReviewIn(BaseModel):
    comment: str = Field(None, max_length=250)
    rating:int = Field(..., ge=0, lt=11)
    productId:UUID = None

    
class ReviewOut(BaseModel):
    id: UUID 
    created_at: datetime
    