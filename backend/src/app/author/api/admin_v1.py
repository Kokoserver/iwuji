import typing as t
import uuid

from fastapi import APIRouter, Query, Response, status
from src.app.author import schema, service

from src.base.enum.sort_type import SortOrder
from src.base.schema.response import ResponseMessage

router = APIRouter(prefix="/authors", tags=["book Authors"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_author(data_in: schema.IAuthorIn) -> ResponseMessage:
    return await service.create_author(data_in)


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


@router.get(
    "/{author_id}", response_model=schema.IAuthorOut, status_code=status.HTTP_200_OK
)
async def get_author_data(author_id: int) -> schema.IAuthorOut:
    return await service.get_author(author_id)


@router.put("/{author_id}", status_code=status.HTTP_200_OK)
async def update_author(
    data_in: schema.IAuthorIn, author_id: uuid.UUID
) -> ResponseMessage:
    return await service.update_author(data_in=data_in, author_id=author_id)


@router.delete("/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_author(author_id: uuid.UUID) -> Response:
    return await service.remove_author_data(author_id)
