from pydantic import BaseModel, IPvAnyAddress


class CheckUserEmail(BaseModel):
    email:str
    class Config:
        arbitrary_types_allowed = True

class AuthSchemaUpdate(BaseModel):
    Ip:IPvAnyAddress

class _Base_type(BaseModel):
    refresh_token: str



class TokenData(_Base_type):
    access_token: str
    token_type: str = "bearer"


class UserRefreshTokenInput(_Base_type):
    pass


class UpdateUserInput(BaseModel):
    userId: str

class ToEncode(BaseModel):
    id:str
    firstname:str
    is_active:bool 
    