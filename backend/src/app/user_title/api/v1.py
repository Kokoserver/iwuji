import typing as t
from fastapi import APIRouter, status, Query
from src.base.enum.sort_type import SortOrder
from src.app.user_title import schema, service


router = APIRouter(prefix="/titles", tags=["User titles"])


@router.get(
    "/",
    response_model=t.List[schema.ITitleOut],
    status_code=status.HTTP_200_OK,
)
async def get_title_list(
    filter: t.Optional[str] = Query(
        default="", alias="filter", description="filter all attributes"
    ),
    select: t.Optional[str] = Query(
        default="",
        alias="select",
        description="specific attributes",
    ),
    per_page: int = 10,
    page: int = 1,
    sort_by: t.Optional[SortOrder] = Query(
        default=SortOrder.desc, description="order by attribute, e.g. id"
    ),
    order_by: t.Optional[str] = Query(
        default="id", description="order by attribute, e.g. id"
    ),
) -> t.List[schema.ITitleOut]:
    return await service.filter(
        filter=filter,
        per_page=per_page,
        page=page,
        select=select,
        sort_by=sort_by,
        order_by=order_by,
    )
