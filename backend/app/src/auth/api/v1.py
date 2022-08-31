from fastapi import APIRouter, BackgroundTasks, Depends, status
from fastapi.requests import Request
from fastapi.security import OAuth2PasswordRequestForm
from app.src._base.schemas import Message
from app.src.auth import crud
from app.src.auth import schemas

auth = APIRouter()


@auth.post("/login", response_model=schemas.TokenData, status_code=status.HTTP_200_OK,)
async def auth_login(request: Request,
                     background_task: BackgroundTasks,
                     auth_data: OAuth2PasswordRequestForm = Depends()) -> schemas.TokenData:
    return await crud.auth_login(background_task, request, auth_data)


@auth.post("/token-refresh", status_code=status.HTTP_200_OK,)
# response_model = schemas.TokenData
async def auth_login_token_refresh(user_token: schemas.UserRefreshTokenInput, request: Request) -> schemas.TokenData:
    return await crud.auth_login_token_refresh(user_token, request)


@auth.post("/check/dev", status_code=status.HTTP_200_OK, response_model=Message)
async def check_user_email(user_data: schemas.CheckUserEmail) -> Message:
    return await crud.check_user_email(user_data)