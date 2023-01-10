from uuid import UUID
from pydantic import BaseModel, Field


class PermissionIn(BaseModel):
    name: str = Field(..., description="Name of the permission", max_length=20)


class PermissionOut(BaseModel):
    id: int = Field(..., description="Id of the permission")
    name: str = Field(..., description="Name of the permission", max_length=20)
