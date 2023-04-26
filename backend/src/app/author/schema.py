import typing as t
import uuid
import pydantic as pyd


class IAuthorIn(pyd.BaseModel):
    title_id: uuid.UUID
    firstname: str
    lastname: str
    email: pyd.EmailStr
    short_description: str
    full_description: str
    cover_img: t.Optional[str] = pyd.Field(description="image uri")


class IAuthorOut(IAuthorIn):
    id: uuid.UUID
