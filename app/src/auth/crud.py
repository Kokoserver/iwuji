from uuid import UUID
from fastapi import BackgroundTasks, status, HTTPException
from fastapi.requests import Request
from fastapi.security import OAuth2PasswordRequestForm
from app.core.config import settings
from app.src._base.schemas import Message
from app.core.security import JWTAUTH
from app.lib.mail.mailer import Mailer
from app.src.auth.models import AuthModel
from app.src.user.models import User
from app.src.auth import schemas

async def create_or_update_auth(request: Request, user: User) ->bool:
    ip = request.client.host    
    get_user_auth:AuthModel = await AuthModel.objects.update_or_create(user=user, ip=ip)
    return True if get_user_auth else False



async def auth_login(background_task:BackgroundTasks, request:Request, auth_data:OAuth2PasswordRequestForm) ->schemas.TokenData:
    check_user:User = await User.objects.get_or_none(email=auth_data.username)
    if not check_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="incorrect email or password")

    if not check_user.check_password(auth_data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="incorrect email or password")
    if check_user.is_active:
        get_jwt_data_for_encode = schemas.ToEncode(
            id=check_user.id, 
            firstname=check_user.firstname, 
            is_active=check_user.is_active
            )
        access_token, refresh_token = JWTAUTH.JwtEncoder(data=get_jwt_data_for_encode.dict())
        _ = await create_or_update_auth(request, check_user)
        return  schemas.TokenData(access_token=access_token, refresh_token=refresh_token)
    token:str = JWTAUTH.DataEncoder(data={"id":check_user.id})
    mail_template_context = {
            "url":f"{settings.PROJECT_URL}/user/{token}/confirmation",
            "button_label": "confirm",
            "title":"user email confirmation link",
            "description":f"""Welcome to <b>{settings.PROJECT_URL}</b>, 
            kindly click on the link below to activate your account""",
        }
        
    new_mail = Mailer(
            website_name=settings.PROJECT_NAME,
            template_name="action.html",
            subject="Email confirmation",
            context=mail_template_context)
    background_task.add_task(new_mail.send_mail, email=[check_user.email])
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Account is not verified, please check your email for verification link"
    )



async def auth_login_token_refresh(user_token: schemas.UserRefreshTokenInput, request:Request) -> schemas.TokenData:
    token_data = JWTAUTH.data_decoder(encoded_data=user_token.refresh_token)
    id = token_data.get("id")
    check_user: User = await User.objects.get_or_none(id = id)
    if not check_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account does not exist",
        )
    get_user_auth:AuthModel  = await AuthModel.objects.get_or_none(user = check_user)
    if request.client.host != get_user_auth.ip:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid issuer device or ip",
        )
    
    _ = await create_or_update_auth(request, check_user)
    access_token, refresh_token = JWTAUTH.JwtEncoder(data={"id": check_user.id})
    return schemas.TokenData(access_token=access_token, refresh_token=refresh_token)


async def check_user_email(user_data:schemas.CheckUserEmail) -> Message:
    check_user:User = await User.objects.get_or_none(email=user_data.email)
    if not check_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account does not exist",
        )
    return  Message(message="Account exists")