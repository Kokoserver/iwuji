from typing import Optional
from pydantic import BaseModel

class MediaBase(BaseModel):
    alt: Optional[str]
    url:Optional[str]
    content_type:Optional[str]
    
    
class MediaCreate(BaseModel):
    alt: str
    url:str
    content_type:str

class MediaUpdate(BaseModel):
    alt: str
    url:str
    content_type:str

class MediaOut(MediaBase):
    id:int
    created_at: str