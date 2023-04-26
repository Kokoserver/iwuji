import typing as t
from fastapi import status
from fastapi.responses import JSONResponse


def response_data(
    data: t.Union[t.AnyStr, t.Dict, t.List], status: int = status.HTTP_200_OK
):
    JSONResponse()
