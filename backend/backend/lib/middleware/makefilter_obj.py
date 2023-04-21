from fastapi import Request, Response
from pydantic import BaseModel


class Params(BaseModel):
    select: str
    filter: str
    order_by: str


async def make_filter_middleware(request: Request, call_next):
        query_params = request.query_params
        select = query_params.select if query_params.select else ''
        filter = query_params.filter if query_params.filter else ''
        order_by = query_params.order_by if query_params.order_by else ''
    #     params = Params(select=query_params.select,
    #                     filter=query_params.filter,
    #                     order_by=query_params.order_by)
        if select or filter or order_by:
            selectList = select.replace(".", "__").split(",")
            order_by = [f'-{attr.replace(".", "__")}' for attr in order_by.split(",")]
            filter_obj = dict()
            for item in filter.replace(".", "__").split(","):
                attr = item.split("=")
                filter_obj[f'{attr[0]}__icontains'] = attr[1]
            request.meta = dict(selectList=selectList,
                                order_by=order_by, filter_obj=filter_obj)
    print(request.query_params)
    response: Response = await call_next(request)
    return response
