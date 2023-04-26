import typing as t
import uuid
import pydantic as pyd


class ITitleIn(pyd.BaseModel):
    name: pyd.constr(max_length=10, strip_whitespace=True)


class ITitleOut(pyd.BaseModel):
    id: t.Optional[uuid.UUID]
    name: t.Optional[str]

    class Config:
        orm_mode = True
