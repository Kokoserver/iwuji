from typing import List
from uuid import UUID
from fastapi import Response, status, HTTPException
from .._base.schemas import Message
from app.src.permission.models import Permission
from app.src.permission import schemas


# create permission
async def create_permission(permission: schemas.PermissionIn)->Message:
    _, created= await Permission.get_or_create(name=permission.name)
    if not created:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Permission already exists")
    return  Message(message="Permission created successfully")
    
        
# get permission
async def get_permission(*, id: UUID) -> Permission:
    perm = await Permission.filter(id=id).first()
    if perm:
        return  perm
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Permission does not exist")


# get all permissions
async def get_all_permissions(filter:str, limit:int = 10, offset:int = 0)->List[Permission]:
      return await Permission.filter(name__icontains=filter).offset(offset).limit(limit)
      

# update permission
async def update_permission(*, id: UUID, permission: schemas.PermissionIn)->Permission:
    check_per = await Permission.filter(id=id).first()
    if not check_per:
        raise HTTPException( status_code=status.HTTP_400_BAD_REQUEST, detail="Permission does not exist")
    
    if await Permission.filter(name=permission.name):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Permission already exists")
    for key, value in permission.dict().items():
        if value != None:
            setattr(check_per, key, value)
    updated_per = await check_per.save()
    return Message(message="Permission updated successfully")
    

    

# delete permission
async def delete_permission(*, id: UUID)->None:
    check_per = await Permission.filter(id=id).first()
    if check_per:
        await check_per.delete()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Permission does not exist")


