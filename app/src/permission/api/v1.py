from typing import List
from uuid import UUID
from fastapi import APIRouter, status
from ..._base.schemas import Message
from app.src.permission.schemas import PermissionIn, PermissionOut
from app.src.permission import crud

perm = APIRouter()

@perm.post("/", response_model=Message, status_code=status.HTTP_201_CREATED)
async def create_permission(permission: PermissionIn)->PermissionOut:
    return await crud.create_permission(permission=permission)

@perm.get("/", response_model=List[PermissionOut] )
async def get_all_permissions(filter:str = '', limit:int = 10, offset:int = 0)->List[PermissionIn]:
    return await crud.get_all_permissions(filter=filter, limit=limit, offset=offset)

@perm.get("/{id}", response_model=PermissionOut)
async def get_permission(id: UUID)->PermissionOut:
    return await crud.get_permission(id=id)

@perm.put("/{id}", response_model=Message)
async def update_permission(id: UUID, permission: PermissionIn)->Message:
    return await crud.update_permission(id=id, permission=permission)

@perm.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_permission(id: UUID)->None:
    return await crud.delete_permission(id=id)
