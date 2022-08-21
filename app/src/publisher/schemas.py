from typing import Optional
from uuid import UUID
import pydantic
from app.src.user.schemas import UserDataOut
from app.src.media.schemas import MediaBase
from app.utils import pydanticForm

from .enum import PublisherTitle


class PublisherBase(pydantic.BaseModel):
    email: pydantic.EmailStr
    title : Optional[PublisherTitle] = PublisherTitle.DR
    description : str

 
@pydanticForm.as_form
class PublisherIn(PublisherBase):
    pass
    
class PublisherOut(PublisherBase):
    id : UUID
    details : UserDataOut
    profile_img : Optional[MediaBase]
    
