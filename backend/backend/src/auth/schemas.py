import pydantic


class CheckUserEmail(pydantic.BaseModel):
    email: str

    class Config:
        arbitrary_types_allowed = True


class AuthSchemaUpdate(pydantic.BaseModel):
    Ip: pydantic.IPvAnyAddress


class _Base_type(pydantic.BaseModel):
    refresh_token: str


class TokenData(_Base_type):
    access_token: str
    token_type: str = "bearer"


class UserRefreshTokenInput(_Base_type):
    pass


class UpdateUserInput(pydantic.BaseModel):
    userId: int


class ToEncode(pydantic.BaseModel):
    id: int
    firstname: str
    is_active: bool
