from datetime import timedelta
from typing import List
from uuid import UUID
from fastapi import HTTPException, Response, status
from fastapi.background import BackgroundTasks
from app.core import security
from app.core import config
from app.src.user import schemas 
from app.src.permission.models import  Permission
from app.src.user.models import User
from app.src._base.schemas import Message
from app.lib.mail.mailer import Mailer
from tortoise.models import Q

async def create_user(new_user_data: schemas.UserRegisterInput,background_task: BackgroundTasks) -> Message:
    check_user: User = await User.filter(email=new_user_data.email).first()
    if check_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Account already exist")
    get_perm, _ = await Permission.get_or_create(name="customer")
    new_user:User = await User(**new_user_data.dict(), role=get_perm)
    new_user.hash_password()
    await new_user.save()
    if new_user:
        token:str = security.JWTAUTH.DataEncoder(data={"id": str(new_user.id)})
        mail_template_context = {
            "url":f"{config.settings.PROJECT_URL}/user/{token}/confirmation",
            "button_label": "confirm",
            "title":"user email confirmation link",
            "description":f"""Welcome to <b>{config.settings.PROJECT_URL}</b>, 
            kindly click on the link below to activate your account""",
        }
        
        new_mail = Mailer(
            website_name=config.settings.PROJECT_NAME,
            template_name="action.html",
            subject="Email confirmation",
            context=mail_template_context)
        background_task.add_task(new_mail.send_mail, email=[new_user.email])
        return Message(
            message="Account was created successfully, an email confirmation link has been to your mail"
        )



async def verify_user_email(user_token: schemas.UserAccountVerifyToken) -> Message:
    data: dict = security.JWTAUTH.data_decoder(encoded_data=user_token.token)
    id = UUID(data.get("id", None))
    if data and id:
        user_obj:User = await User.get_or_none(id=id)
        if user_obj and user_obj.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Account has been already activated")
        if user_obj:
            user_obj.is_active=True
            await user_obj.save()
            return Message(message="Account was activated successfully")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Account does not exist")
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Invalid token was provided")



async def reset_password_link(background_task: BackgroundTasks,user_data: schemas.GetPasswordResetLink)->Message:
    user_obj: User = await User.get_or_none(email=user_data.email)
    if not user_obj:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Account does not exist")
    if user_obj:
        token = security.JWTAUTH.DataEncoder(data={"id": str(user_obj.id)}, duration=timedelta(days=1))
        mail_template_context = {
            "url":f"{config.settings.PROJECT_URL}/user/{token}/password-reset",
            "button_label":"reset password",
            "title":"password reset link",
            "description":"You request for password reset link, if not you please contact admin",
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
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password do not match")
    token_data: dict = security.JWTAUTH.data_decoder(encoded_data=user_data.token)
    id=UUID(token_data.get("id", None))
    if token_data and id:
        user_obj: User = await User.get_or_none(id = id)
        if user_obj.check_password(user_data.password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Try another password, password already used")
        new_password:str = user_obj.generate_hash(user_data.password)
        user_obj.password=new_password
        await user_obj.save()
        return Message(message="password was reset successfully")
    raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid token was provided",
        )


async def get_current_user_data(userid:int) -> User:
    user_data = await User.get_or_none(id=userId)
    if not user_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist")
    return user_data

async def get_users(limit, offset, filter) -> List[User]:
    if isinstance(filter, str):
        all_user = await User.filter(
            Q(email__icontains=filter )|
            Q(firstname__icontains=filter) | 
            Q(lastname__icontains=filter)|
            Q(role__name__icontains=filter)            
        ).offset(offset).limit(limit)
    try:
     if isinstance(bool(filter), bool):
        all_user = await User.filter(is_active=filter).offset(offset).limit(limit).all()
    except Exception as e:
        pass
    try:
        uuid = UUID(filter)
    except Exception:
        uuid = None
    if uuid:
        all_user = await User.filter(id=uuid).offset(offset).limit(limit)
    return all_user



async def remove_user_data(userid:int) -> None:
    user_to_remove = await User.filter(id=userId).first()
    if user_to_remove:
        await user_to_remove.delete()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with id {userId} does not exist",
    )
    
async def get_user(userid:int) -> Message:
    use_detail:User = await User.filter(id=userId).select_related("role").first()
    if use_detail:
        return use_detail
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with id {userId} does not exist",
    )
    
async def add_user_role(userid:int, role: str) -> User:
    user_to_update:User = await User.filter(id=userId).select_related("role").first()
    if not user_to_update:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with id {userId} does not exist",
    )
        
    if user_to_update.role.name == role:
        raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"User with id {userId} already has {role} role",
    )
    check_per:Permission = await Permission.get_or_none(name=role)
    if not check_per:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Permission with name {role} does not exist",
    )
    setattr(user_to_update, "role", check_per)
    await user_to_update.save()
    return Message(message="User role was updated successfully")
    
    
  
async def remove_user_role(userid:int, role: str) -> None:
    check_user:User = await User.filter(id=userId).select_related("role").first()
    if not check_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User does not exist",
            )
    if not check_user.role.name == role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Permission with name {role} does not exist for user with id {userId}",
            )
    check_user.role = await Permission.filter(name="customer").first()
    await check_user.save()
    return Message(message="User role was updated successfully")
    
async def get_user_role(userid:int) -> Permission:
    check_user:User = await User.filter(id=userId).select_related("role").first()
    if check_user:
        return check_user.role
    raise HTTPException( status_code=status.HTTP_404_NOT_FOUND,detail="User role does not exist")
        
            
          
        


    