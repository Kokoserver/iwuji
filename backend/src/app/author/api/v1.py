import typing as t
from fastapi import APIRouter, Query
from src.app.author import schema, service

from src.base.enum.sort_type import SortOrder

router = APIRouter(prefix="/authors", tags=["book Authors"])


@router.get("/", response_model=list[schema.IAuthorOut])
async def get_authors_list(
    filter: t.Optional[str] = Query(
        default="", alias="filter", description="filter all authora"
    ),
    select: t.Optional[str] = Query(
        default="",
        alias="select",
        description="specific attributes of the authors",
    ),
    per_page: int = 10,
    page: int = 1,
    sort_by: t.Optional[SortOrder] = Query(
        default=SortOrder.desc, description="order by attribute, e.g. id"
    ),
    order_by: t.Optional[str] = Query(
        default="id", description="order by attribute, e.g. id"
    ),
    load_content: bool = False,
):
    return await service.filter(
        filter=filter,
        per_page=per_page,
        page=page,
        select=select,
        order_by=order_by,
        sort_by=sort_by,
        load_related=load_content,
    )
