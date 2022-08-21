from datetime import datetime
from uuid import UUID
import pydantic
from pydantic import BaseModel



class Base_types(pydantic.BaseModel):
    email: pydantic.EmailStr
    



class UserRegisterInput(Base_types):
    firstname: str = pydantic.Field(min_length=2)
    lastname: str = pydantic.Field(min_length=2)
    password:str = pydantic.Field(min_length=5)




class GetPasswordResetLink(Base_types):
    pass



class PasswordResetInput(pydantic.BaseModel):
    token: str
    password: str
    confirm_password: str
    


class UserLoginInput(pydantic.BaseModel):
    username: pydantic.EmailStr
    password: bytes
    



class UserDataOut(BaseModel):
    id: UUID
    email: pydantic.EmailStr
    firstname: str
    lastname: str
    is_active:bool
    created_at :datetime
    class Config:
        orm_mode = True
        
    
    
class UserDataOutForPost(pydantic.BaseModel):
    id: int
    email: pydantic.EmailStr
    firstname: str
    lastname: str


class UserAccountVerifyToken(pydantic.BaseModel):
    token: str
    