import typing as t
import uuid
from fastapi import status, Response
from src.base.enum.sort_type import SortOrder
from src.lib.errors import error
from src.app.user_title import schema, model
from src.app.user_title.repository import user_title_repo


async def create(data_in: schema.ITitleIn) -> model.UserTitle:
    check_title = await user_title_repo.get_by_attr(
        attr=dict(name=data_in.name), first=True
    )
    if check_title:
        raise error.DuplicateError("title already exists")
    new_title = await user_title_repo.create(data_in)
    return new_title


async def get(
    title_id: uuid.UUID,
):
    get_title = await user_title_repo.get(title_id)
    if not get_title:
        raise error.NotFoundError("UserTitle not found")
    return get_title


async def update(title_id: uuid.UUID, data_in: schema.ITitleIn):
    get_title = await user_title_repo.get(title_id)
    if not get_title:
        raise error.NotFoundError("Title not found")
    check_title = await user_title_repo.get_by_attr(
        attr=dict(name=data_in.name), first=True
    )
    if check_title and check_title.id != title_id:
        raise error.DuplicateError(" Title already exists")
    if get_title.name == data_in.name:
        return get_title
    return await user_title_repo.update(title_id, data_in)


async def filter(
    filter: str = "",
    per_page: int = 10,
    page: int = 0,
    select: str = "",
    sort_by: SortOrder = SortOrder.asc,
    order_by: str = None,
) -> t.List[model.UserTitle]:
    get_categories = await user_title_repo.filter(
        filter_string=filter,
        per_page=per_page,
        page=page,
        select_columns=select,
        sort_by=sort_by,
        order_by=order_by,
    )
    return get_categories


async def delete(
    title_id: str,
):
    get_title = await user_title_repo.get(title_id)
    if not get_title:
        raise error.NotFoundError("Title not found")
    await user_title_repo.delete(title_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
