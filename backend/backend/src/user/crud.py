from datetime import timedelta
from typing import List
from fastapi import HTTPException, Response, status
from fastapi.background import BackgroundTasks
from backend.core import security
from backend.core import config
from backend.src.user import schemas
from backend.src.permission.models import Permission
from backend.src.user.models import User
from backend.src._base.schemas import Message
from backend.lib.mail.mailer import Mailer
from ormar import or_


async def create_user(
        new_user_data: schemas.UserRegisterInput, background_task: BackgroundTasks
) -> Message:
    check_user: User = await User.objects.get_or_none(email=new_user_data.email)
    if check_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Account already exist"
        )
    get_perm, _ = await Permission.objects.get_or_create(name="customer")
    new_user: User = User(**new_user_data.dict(), role=get_perm)
    new_user.hash_password()
    await new_user.save()
    if new_user:
        token: str = security.JWTAUTH.DataEncoder(data={"user_id": str(new_user.id)})
        mail_template_context = {
            "url": f"{config.settings.PROJECT_URL}/auth/activateAccount?activate_token={token}",
            "button_label": "confirm",
            "title": "user email confirmation link",
            "description": f"""Welcome to <b>{config.settings.PROJECT_URL}</b>, 
            kindly click on the link below to activate your account""",
        }

        new_mail = Mailer(
            website_name=config.settings.PROJECT_NAME,
            template_name="action.html",
            subject="Email confirmation",
            context=mail_template_context,
        )
        background_task.add_task(new_mail.send_mail, email=[new_user.email])
        return Message(
            message="Account was created successfully, an email confirmation link has been to your mail"
        )


async def verify_user_email(user_token: schemas.UserAccountVerifyToken) -> Message:
    data: dict = security.JWTAUTH.data_decoder(encoded_data=user_token.token)
    id = data.get("user_id", None)
    if data and id:
        user_obj: User = await User.objects.get_or_none(id=int(id))
        if user_obj and user_obj.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Account has been already verified",
            )
        if user_obj:
            await user_obj.update(is_active=True)
            return Message(message="Account was verified successfully")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token was provided"
        )
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token was provided"
    )


async def reset_password_link(
        background_task: BackgroundTasks, user_data: schemas.GetPasswordResetLink
) -> Message:
    user_obj: User = await User.objects.get_or_none(email=user_data.email)
    if not user_obj:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Account does not exist"
        )
    if user_obj:
        token = security.JWTAUTH.DataEncoder(
            data={"user_id": user_obj.id}, duration=timedelta(days=1)
        )
        mail_template_context = {
            "url": f"{config.settings.PROJECT_URL}/auth/passwordReset?reset_token={token}",
            "button_label": "reset password",
            "title": "password reset link",
            "description": "You request for password reset link, if not you please contact admin",
        }
        new_mail = Mailer(
            website_name=config.settings.PROJECT_NAME,
            template_name="action.html",
            context=mail_template_context,
            subject="Password reset link",
        )
        background_task.add_task(new_mail.send_mail, email=[user_obj.email])
        return Message(
            message="password reset token has been sent to your email, link expire after 24 hours"
        )


async def update_user_password(user_data: schemas.PasswordResetInput) -> Message:
    if not user_data.password == user_data.confirm_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Password do not match"
        )
    token_data: dict = security.JWTAUTH.data_decoder(encoded_data=user_data.token)
    id = token_data.get("user_id", None)
    if token_data and id:
        user_obj: User = await User.objects.get_or_none(id=int(id))
        if user_obj.check_password(user_data.password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Try another password, password already used",
            )
        new_password: str = user_obj.generate_hash(user_data.password)
        user_obj.password = new_password
        await user_obj.upsert()
        return Message(message="password was reset successfully")
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Invalid token was provided",
    )


async def get_current_user_data(userId: int) -> User:
    user_data = await User.objects.select_related("role").get_or_none(id=userId)
    if not user_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist"
        )
    return user_data


async def get_users(limit, offset, filter, id: int, is_active: bool) -> List[User]:
    if isinstance(filter, str):
        all_user = (
            await User.objects.filter(
                or_(
                    email__icontains=filter,
                    firstname__icontains=filter,
                    lastname__icontains=filter,
                    role__name__icontains=filter,
                    id=id,
                    is_active=is_active,
                )
            )
            .offset(offset)
            .limit(limit)
        )

        return all_user
    return []


async def remove_user_data(userId: int) -> None:
    user_to_remove = await User.objects.get_or_none(id=userId)
    if user_to_remove:
        await user_to_remove.delete()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with user_id {userId} does not exist",
    )


async def get_user(userId: int) -> Message:
    use_detail: User = await User.objects.select_related(["role"]).get_or_none(
        id=userId
    )
    if use_detail:
        return use_detail
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with user_id {userId} does not exist",
    )


async def add_user_role(data: schemas.UserPermissionUpdate) -> User:
    user_to_update: User = await User.objects.select_related(["role"]).get_or_none(
        id=data.user_id
    )
    if not user_to_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with user_id {data.user_id} does not exist",
        )

    if user_to_update.role.name == data.role:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User with user_id {data.user_id} already has {data.rol} role",
        )
    check_per: Permission = await Permission.objects.get_or_none(name=data.role)
    if not check_per:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Permission with name {data.role} does not exist",
        )
    setattr(user_to_update, "role", check_per)
    await user_to_update.upsert()
    return Message(message="User role was updated successfully")


async def get_user_role(userId: int) -> Permission:
    check_user: User = await User.objects.select_related(["role"]).get_or_none(
        id=userId
    )
    if check_user:
        return check_user.role
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="User role does not exist"
    )


async def remove_user_role(data: schemas.UserPermissionUpdate) -> None:
    check_user: User = await User.objects.select_related(["role"]).get_or_none(
        id=data.user_id
    )
    if not check_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User does not exist",
        )
    if not check_user.role.name == data.role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Permission with name {data.role} does not exist for user with user_id {data.user_id}",
        )
    check_user.role = await Permission.objects.get_or_none(name="customer")
    await check_user.upsert()
    return Message(message="User role was updated successfully")
