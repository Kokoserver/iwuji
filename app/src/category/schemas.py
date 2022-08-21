from uuid import UUID
from pydantic import BaseModel

class CategoryIn(BaseModel):
    name:str 
    
class CategoryOut(BaseModel):
    id : UUID
    name:str 
    class Config:
        orm_mode = True