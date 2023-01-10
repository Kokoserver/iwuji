from fastapi import Request, status
from starlette.responses import JSONResponse, Response
from starlette.concurrency import iterate_in_threadpool


async def gen_range(s):
    import json
    errors = json.loads(s)
    data = {'detail': {k.get("loc")[-1]: k.get("msg") for k in errors['detail']}}
    return data


async def catch_exceptions_middleware(request: Request, call_next):
    response: Response = await call_next(request)
    if response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR:
        return JSONResponse(
            status_code=response.status_code,
            content='Internal server error',
            media_type=response.media_type
        )
    if response.status_code >= status.HTTP_422_UNPROCESSABLE_ENTITY:
        response_body = [chunk async for chunk in response.body_iterator]
        response.body_iterator = iterate_in_threadpool(iter(response_body))
        data = await gen_range(response_body[0].decode())
        return JSONResponse(
            status_code=response.status_code,
            content=data,
            media_type=response.media_type
        )
    return response
