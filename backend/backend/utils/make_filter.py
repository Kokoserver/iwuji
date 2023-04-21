from pydantic import BaseModel


class Params(BaseModel):
    select: list = []
    filter_obj: dict = {}
    order_by: list = []


def make_filter(filter: str = '', order_by: str = '', select: str = ''):
    select = [item.strip() for item in select.replace(".", "__").split(",") if select]
    print(select)
    order_by = [
        f'-{attr.replace(".", "__")}' for attr in order_by.split(",") if attr
    ] if order_by else []
    filter_obj = dict()
    if filter:
        for item in filter.replace(".", "__").split(","):
            attr = item.split("=")
            filter_obj[f'{attr[0]}__icontains'] = attr[1]
    data = Params(select=select, order_by=order_by, filter_obj=filter_obj)
    return data
