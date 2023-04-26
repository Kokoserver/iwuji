import typing as t
import uuid
from fastapi import status, Response
from src.base.enum.sort_type import SortOrder
from src.lib.errors import error
from src.app.category import schema, model
from src.app.category.repository import category_repo


async def create(data_in: schema.ICategoryIn) -> model.Category:
    check_category = await category_repo.get_by_attr(attr=dict(name=data_in.name), first=True)
    if check_category:
        raise error.DuplicateError("category already exists")
    new_category = await category_repo.create(data_in)
    return new_category


async def get(
    category_id: uuid.UUID,
):
    get_category = await category_repo.get(category_id)
    if not get_category:
        raise error.NotFoundError("Category not found")
    return get_category


async def update(category_id: uuid.UUID, data_in: schema.ICategoryIn):
    get_category = await category_repo.get(category_id)
    if not get_category:
        raise error.NotFoundError("Category not found")
    check_category = await category_repo.get_by_attr(attr=dict(name=data_in.name), first=True)
    if check_category and check_category.id != category_id:
        raise error.DuplicateError("Category already exists")
    if get_category.name == data_in.name:
        return get_category
    return await category_repo.update(category_id, data_in)


async def filter(
    filter: str = "",
    per_page: int = 10,
    page: int = 0,
    select: str = "",
    sort_by: SortOrder = SortOrder.asc,
    order_by: str = None,
) -> t.List[model.Category]:
    get_categories = await category_repo.filter(
        filter_string=filter,
        per_page=per_page,
        page=page,
        select_columns=select,
        sort_by=sort_by,
        order_by=order_by,
    )
    return get_categories


async def delete(
    category_id: str,
):
    get_category = await category_repo.get(category_id)
    if not get_category:
        raise error.NotFoundError("Category not found")
    await category_repo.delete(category_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
