from typing import List
from fastapi import APIRouter, BackgroundTasks, Depends, status
from backend.src._base.schemas import Message
from backend.shared.dependency import UserWrite
from backend.src.user import schemas, crud
from backend.src.permission.schemas import PermissionOut
from backend.src.user.models import User

user = APIRouter()


@user.post("/register", status_code=status.HTTP_201_CREATED, response_model=Message)
async def create_user(user: schemas.UserRegisterInput, background_task: BackgroundTasks) -> Message:
    return await crud.create_user(user, background_task)


@user.get("/", response_model=List[schemas.UserDataOut], status_code=status.HTTP_200_OK)
async def get_users(id: int = "", is_active: bool = True, limit: int = 10, offset: int = 0, filter: str = '',
                    _: int = Depends(UserWrite.super_or_admin)) -> List[schemas.UserDataOut]:
    return await crud.get_users(limit, offset, filter, id, is_active)


@user.get("/{user_id}/data", response_model=schemas.UserDataOut, status_code=status.HTTP_200_OK)
async def get_user(user_id: int, _: int = Depends(UserWrite.super_or_admin)) -> schemas.UserDataOut:
    return await crud.get_user(user_id)


@user.get("/whoami", response_model=schemas.UserDataOut, status_code=status.HTTP_200_OK)
async def get_user_current_user_data(user_id: int = Depends(UserWrite.current_user)) -> schemas.UserDataOut:
    print("here")
    return await crud.get_current_user_data(user_id)


@user.post("/passwordResetLink", status_code=status.HTTP_200_OK)
async def reset_password_link(user_data: schemas.GetPasswordResetLink, background_task: BackgroundTasks) -> Message:
    return await crud.reset_password_link(background_task, user_data)


@user.post("/account/activate", status_code=status.HTTP_200_OK)
async def verify_user_email(user_data: schemas.UserAccountVerifyToken) -> Message:
    return await crud.verify_user_email(user_data)


@user.put("/", status_code=status.HTTP_200_OK)
async def update_user_password(user_data: schemas.PasswordResetInput) -> Message:
    return await crud.update_user_password(user_data)


@user.delete("/{userId}", status_code=status.HTTP_200_OK)
async def delete_user(userId: str, _: User = Depends(UserWrite.is_super_admin)) -> None:
    return await crud.remove_user_data(userId)


@user.get("/{user_id}/role", response_model=PermissionOut)
async def get_user_roles(user_id: int, _: int = Depends(UserWrite.super_or_admin)):
    return await crud.get_user_role(user_id)


@user.put("/role", status_code=status.HTTP_200_OK)
async def update_user_role(data: schemas.UserPermissionUpdate, _: int = Depends(UserWrite.super_or_admin)) -> Message:
    return await crud.add_user_role(data)


@user.delete("/role", status_code=status.HTTP_200_OK)
async def remove_user_role(data: schemas.UserPermissionUpdate, _: int = Depends(UserWrite.is_super_admin)) -> Message:
    return await crud.remove_user_role(data)
