from typing import List
from fastapi import Response, status, HTTPException
from app.src._base.schemas import Message
from app.src.permission.models import Permission
from app.src.permission import schemas


# create permission
async def create_permission(permission: schemas.PermissionIn)->Message:
    _, created = await Permission.objects.get_or_create(name=permission.name)
    if not created:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Permission already exists")
    return Message(message="Permission created successfully")


# get permission
async def get_permission(*, id: int) -> Permission:
    perm = await Permission.objects.get_or_none(id=id)
    if perm:
        return perm
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Permission does not exist")


# get all permissions
async def get_all_permissions(filter: str, limit: int = 10, offset: int = 0)->List[Permission]:
    return await Permission.objects.filter(name__icontains=filter).offset(offset).limit(limit).all()


# update permission
async def update_permission(*, id: int, permission: schemas.PermissionIn)->Permission:
    check_per = await Permission.objects.get_or_none(id=id)
    if not check_per:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Permission does not exist")

    if await Permission.objects.filter(name=permission.name).exists():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Permission already exists")
    for key, value in permission.dict().items():
        if value != None:
            setattr(check_per, key, value)
    await check_per.upsert()
    return Message(message="Permission updated successfully")


# delete permission
async def delete_permission(*, id: int)->None:
    check_per = await Permission.objects.get_or_none(id=id)
    if check_per:
        await check_per.delete()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Permission does not exist")
