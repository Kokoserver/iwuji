from typing import List
from uuid import UUID
from fastapi import APIRouter, BackgroundTasks, Depends, status
from app.src._base.schemas import Message
from app.shared.dependency import UserWrite
from app.src.user import schemas, crud
from app.src.permission.schemas import PermissionOut
from app.src.user.models import User


user = APIRouter()

@user.post("/register", status_code=status.HTTP_201_CREATED)
async def create_user(user: schemas.UserRegisterInput, background_task: BackgroundTasks)->Message:
    return await crud.create_user(user, background_task)

@user.get("/", response_model=List[schemas.UserDataOut], status_code=status.HTTP_200_OK)
async def get_users(limit:int = 10, offset:int = 0, filter:str = '', _:UUID = Depends(UserWrite.super_or_admin))->List[schemas.UserDataOut]:
    return await crud.get_users(limit, offset, filter)

@user.get("/{user_id}/role", response_model=PermissionOut)
async def get_user_roles(user_id:str, _:str= Depends(UserWrite.super_or_admin)):
    return await crud.get_user_role(user_id)


@user.get("/me", response_model=schemas.UserDataOut, status_code=status.HTTP_200_OK)
async def get_user_current_user_data(user_id:str= Depends(UserWrite.current_user))->schemas.UserDataOut:
    return await crud.get_current_user_data(user_id)

@user.get("/{user_id}", response_model=schemas.UserDataOut, status_code=status.HTTP_200_OK)
async def get_user(user_id:str, _:UUID = Depends(UserWrite.is_admin))->schemas.UserDataOut:
    return await crud.get_user(user_id)


@user.put("/{user_id}/{role}", status_code=status.HTTP_200_OK)
async def update_user_role(user_id:str, role:str,  _:UUID = Depends(UserWrite.super_or_admin))->Message:
    return await crud.add_user_role(user_id, role)

@user.post("/activate", status_code=status.HTTP_200_OK)
async def verify_user_email(user_data:schemas.UserAccountVerifyToken)->Message:
    return await crud.verify_user_email(user_data)

@user.post("/password-reset-link", status_code=status.HTTP_200_OK)
async def reset_password_link(user_data:schemas.GetPasswordResetLink, background_task: BackgroundTasks)->Message:
    return await crud.reset_password_link(background_task, user_data)

@user.put("/", status_code=status.HTTP_200_OK)
async def update_user_password(user_data:schemas.PasswordResetInput)->Message:
    return await crud.update_user_password(user_data)

@user.delete("/{user_id}/{role}", status_code=status.HTTP_200_OK)
async def remove_user_role(user_id:str, role:str, _:UUID = Depends(UserWrite.is_super_admin))->Message:
    return await crud.remove_user_role(user_id, role)

@user.delete("/{userId}", status_code=status.HTTP_200_OK)
async def delete_user(userId:str, _:User = Depends(UserWrite.is_super_admin))->None:
    return await crud.remove_user_data(userId)
