from fastapi import Request, Response, status
from fastapi.background import BackgroundTasks
from src.app.auth.repository import auth_token_repo
from src.app.user.repository import user_repo
from src.lib.utils.cookie_response_token import update_response_cookies
from src.lib.utils.security import JWTAUTH


async def user_auth_middleware(request: Request, call_next) -> Response:
    response: Response = await call_next(request)
    try:
        background_task: BackgroundTasks = BackgroundTasks()
        auth_refresh_token: str = None
        if response.status_code == status.HTTP_401_UNAUTHORIZED:
            auth_refresh_token = request.cookies.get("auth_refresh_token", None)
        if auth_refresh_token is None:
            return response
        check_auth_token = await auth_token_repo.get_by_attr(
            attr=dict(refresh_token=str(auth_refresh_token)), first=True
        )
        if not check_auth_token:
            return response
        token_data = JWTAUTH.data_decoder(encoded_data=auth_refresh_token)
        check_user = await user_repo.get(token_data.get("user_id", None))
        if check_auth_token.ip_address != auth_token_repo.get_user_ip(request):
            return response
        response_data = update_response_cookies(
            user=check_user,
            request=request,
            background_task=background_task,
        )
        if not bool(response_data):
            return response
        if bool(response_data):
            request = response_data
            new_response: Response = await call_next(request)
        return new_response
    except Exception:
        return response
