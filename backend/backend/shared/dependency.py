import typing

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jose
from backend.core import config as base_config
from backend.src.user.models import User


async def get_user_permission(user_id: int, name: str) -> typing.Union[User, None]:
    check_user_per: User = await User.objects.get_or_none(id=user_id, role__name__icontains=name)
    if check_user_per:
        return check_user_per
    return None


async def get_user_data(user_id: int) -> typing.Union[User, None]:
    get_user: User = await User.objects.get_or_none(id=user_id)
    if get_user.is_active:
        return get_user
    return None


Oauth_schema = OAuth2PasswordBearer(
    tokenUrl=f"{base_config.settings.API_PREFIX}/auth/login")


class UserAuth:
    @staticmethod
    async def authenticate(token: str = Depends(Oauth_schema)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload: dict = jose.jwt.decode(
                token=token,
                key=base_config.settings.SECRET_KEY,
                algorithms=[base_config.settings.ALGORITHM],
            )

            if payload is None:
                raise credentials_exception
            if not payload.get("user_id", None) and not payload.get("firstname", None):
                raise credentials_exception
            return payload
        except jose.JWTError:
            raise credentials_exception


class UserWrite:

    @staticmethod
    async def is_admin(user: dict = Depends(UserAuth.authenticate)) -> User:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Only admin can perform this operation",
        )
        admin_user = await get_user_permission(user_id=user.get("user_id", None), name="admin")
        if admin_user:
            return admin_user
        raise exception

    @staticmethod
    async def is_super_admin(user: dict = Depends(UserAuth.authenticate)) -> User:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Only super admin can perform this operation",
        )
        super_user = await get_user_permission(user_id=user.get("user_id", None), name="super_admin")
        if super_user:
            return super_user
        raise exception

    @staticmethod
    async def super_or_admin(user: dict = Depends(UserAuth.authenticate)) -> User:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Only super admin can perform this operation",
        )
        super_user = await get_user_permission(user_id=user.get("user_id", None), name="super_admin")
        admin_user = await get_user_permission(user_id=user.get("user_id", None), name="admin")
        if super_user or admin_user:
            return super_user
        raise exception

    @staticmethod
    async def current_user_with_data(user: dict = Depends(UserAuth.authenticate)):
        active_user = await get_user_data(user_id=user.get("user_id", None))
        if active_user:
            return active_user
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Account is not active")

    @staticmethod
    async def current_user(user: dict = Depends(UserAuth.authenticate)):
        if user.get("user_id", None) and user.get("firstname", None):
            return user.get("user_id", None)
        print(user.get('firstname'))
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Account is not active")
