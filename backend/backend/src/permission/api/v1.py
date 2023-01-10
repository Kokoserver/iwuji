from typing import List
from fastapi import APIRouter, status
from backend.src._base.schemas import Message
from backend.src.permission.schemas import PermissionIn, PermissionOut
from backend.src.permission import crud

perm = APIRouter()


@perm.post("/", response_model=Message, status_code=status.HTTP_201_CREATED)
async def create_permission(permission: PermissionIn) -> PermissionOut:
    return await crud.create_permission(permission=permission)


@perm.get("/", response_model=List[PermissionOut])
async def get_all_permissions(filter: str = '', limit: int = 10, offset: int = 0) -> List[PermissionIn]:
    return await crud.get_all_permissions(filter=filter, limit=limit, offset=offset)


@perm.get("/{user_id}", response_model=PermissionOut)
async def get_permission(id: int) -> PermissionOut:
    return await crud.get_permission(id=id)


@perm.put("/{user_id}", response_model=Message)
async def update_permission(id: int, permission: PermissionIn) -> Message:
    return await crud.update_permission(id=id, permission=permission)


@perm.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_permission(id: int) -> None:
    return await crud.delete_permission(id=id)
