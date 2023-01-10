from typing import Optional
import pydantic
from backend.src.media.schemas import MediaBase
from backend.utils import pydanticForm

from .enum import AuthorTitle


class AuthorBase(pydantic.BaseModel):
    title: Optional[AuthorTitle] = AuthorTitle.DR
    firstname: str
    lastname: str
    email: pydantic.EmailStr
    description: str


@pydanticForm.as_form
class AuthorIn(AuthorBase):
    pass


@pydanticForm.as_form
class AuthorUpdateIn(AuthorBase):
    pass


class AuthorOut(AuthorBase):
    id: int
    profile_img: Optional[MediaBase]
