from typing import List
from fastapi import HTTPException, Response, status, UploadFile, Request
from starlette.responses import Response

from backend.src.media import crud as mediaCrud
from backend.src.author import schemas
from backend.src.author.models import Author
from backend.src._base.schemas import Message
from backend.utils import make_filter
from ormar import or_


async def create_author(new_author_data: schemas.AuthorIn, request: Request, profile_img: UploadFile = None,) -> Message:
    check_author: Author = await Author.objects.get_or_none(email=new_author_data.email)
    if check_author:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Author already exist")
    new_author: Author = Author(**new_author_data.dict())
    if profile_img:
        profile_img_obj = await mediaCrud.upload([profile_img], request)
        new_author.profile_img = profile_img_obj
    new_author = await new_author.save()
    return Message(message="Author was created successfully")


async def get_authors(filter: str = '', limit: str = '', offset: str = '', select: str = '', order_by: str = '') -> List[Author]:
    req_filter: make_filter.Params = make_filter.make_filter(
        filter=filter, select=select, order_by=order_by)
    all_author = await Author.objects.fields(['email', "lastname"]).filter(
        or_(**req_filter.filter_obj)
    ).offset(offset).limit(limit).order_by(req_filter.order_by).first()
    print(all_author)
    return []
    # return all_author


async def update_author(new_author_data: schemas.AuthorIn,
                        request: Request, profile_img: UploadFile = None,) -> Message:
    check_author: Author = await Author.objects.select_related(
        'profile_img').get_or_none(email=new_author_data.email)
    if not check_author:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="incorrect data provided")
    for key, val in new_author_data.dict().items():
        if val is not None:
            setattr(check_author, key, val)
    if profile_img:
        profile_img_obj = await mediaCrud.update([profile_img], [check_author.profile_img], request)
        check_author.profile_img = profile_img_obj
    check_author = await check_author.upsert()
    return Message(message="Author was updated successfully")


async def get_author(authorId: int) -> Author:
    use_detail: Author = await Author.objects.select_related("profile_img").get_or_none(id=authorId)
    if use_detail:
        return use_detail
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Author with id {authorId} does not exist",
    )


async def remove_author_data(authorId: int) -> Response:
    author_to_remove = await Author.objects.get_or_none(id=authorId)
    if author_to_remove:
        await mediaCrud.delete([author_to_remove.profile_img])
        await author_to_remove.delete()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Author with id {authorId} does not exist",
    )
