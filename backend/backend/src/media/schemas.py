import typing
from pydantic import BaseModel


class MediaBase(BaseModel):
    alt: typing.Optional[str]
    url: typing.Optional[str]
    content_type: typing.Optional[str]


class MediaCreate(BaseModel):
    alt: str
    url: str
    content_type: str


class MediaUpdate(BaseModel):
    alt: str
    url: str
    content_type: str


class MediaOut(MediaBase):
    id: int
    created_at: str
