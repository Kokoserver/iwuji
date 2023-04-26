import uuid
import typing as t
from fastapi import status
from src.app.media_store.repository import media_repo
from src.base.enum.sort_type import SortOrder
from src.base.schema.response import ResponseMessage
from src.lib.errors import error
from src.app.author import schema, model
from fastapi import Response
from src.app.author.repository import author_repo


async def create_author(data_in: schema.IAuthorIn) -> ResponseMessage:
    check_author = await author_repo.get_by_attr(
        attr=dict(**data_in.dict(exclude={"cover_img"})), first=True
    )
    if check_author:
        raise error.DuplicateError("Author already exist")
    check_media = await media_repo.get_by_attr(attr=dict(alt=data_in.cover_img))
    if not check_media:
        raise error.NotFoundError("Cover image not found")
    new_author = await author_repo.create(
        obj=dict(
            data_in.dict(
                exclude_unset=True, exclude={"cover_img"}, cover_img_id=check_media.id
            )
        )
    )

    if new_author:
        return ResponseMessage(message="Author was created successfully")
    raise error.InternalServerError("Error creating new author")


async def filter(
    filter: str,
    per_page: int = 10,
    page: int = 0,
    select: str = "",
    sort_by: SortOrder = SortOrder.asc,
    order_by: str = None,
    load_related: bool = False,
) -> t.List[model.Author]:
    get_authors = await author_repo.filter(
        filter_string=filter,
        per_page=per_page,
        page=page,
        select_columns=select,
        order_by=order_by,
        sort_by=sort_by,
        load_related=load_related,
    )
    return get_authors


async def update_author(
    data_in: schema.IAuthorIn, author_id: uuid.UUID
) -> ResponseMessage:
    check_author = await author_repo.get(id=author_id, load_related=True, first=True)
    if not check_author:
        raise error.NotFoundError("Author does not exist")
    check_media = await media_repo.get_by_attr(attr=dict(alt=data_in.cover_img))
    if not check_media:
        raise error.NotFoundError("Cover image not found")
    to_update = dict()
    if check_author.cover_image.id != check_media.id:
        to_update["cover_image_id"] = check_media.id
    updated_author = await author_repo.update(
        check_author.id, obj=dict(**to_update, **data_in.dict(exclude={"cover_img"}))
    )
    if updated_author:
        return ResponseMessage(message="Author was updated successfully")
    raise error.ServerError("Error updating author")


async def get_author(author_id: uuid.UUID) -> model.Author:
    get_author = await author_repo.get(id=author_id, load_related=True, first=True)
    if not get_author:
        raise error.NotFoundError("Author does not exist")
    return get_author


async def remove_author_data(author_id: uuid.UUID) -> Response:
    author_to_remove = await author_repo.get(id=author_id, first=True)
    if not author_to_remove:
        raise error.NotFoundError("Author does not exist")
    await author_repo.delete(author_repo.id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
