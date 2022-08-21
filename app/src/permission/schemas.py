from uuid import UUID
from pydantic import BaseModel, Field

        
class PermissionIn(BaseModel):
    name:str  =  Field(..., description="Name of the permission", max_length=20)
    class Config:
        orm_mode = True

class PermissionOut(BaseModel):
    name:str  =  Field(..., description="Name of the permission", max_length=20)
    id:UUID = Field(..., description="Id of the permission")
