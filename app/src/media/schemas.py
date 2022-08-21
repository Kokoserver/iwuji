from pydantic import BaseModel

class MediaBase(BaseModel):
    alt: str
    url:str
    content_type:str
    
    
class MediaCreate(MediaBase):
    pass

class MediaUpdate(MediaBase):
    pass

class MediaOut(MediaBase):
    id: str
    created_at: str