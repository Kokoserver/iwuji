from typing import List
from fastapi import APIRouter, Depends, status, UploadFile, File, Request
from starlette.responses import Response

from backend.src._base.schemas import Message
from backend.shared.dependency import UserWrite
from backend.src.author import schemas, crud
from backend.src.author.models import Author

author = APIRouter()


@author.post("/", status_code=status.HTTP_201_CREATED)
async def create_author(request: Request, author: schemas.AuthorIn = Depends(schemas.AuthorIn.as_form),
                        profile_img: UploadFile = File(None), _: int = Depends(UserWrite.super_or_admin)) -> Message:
    return await crud.create_author(author, request, profile_img)


@author.get("/", response_model=List[schemas.AuthorOut], status_code=status.HTTP_200_OK)
async def get_authors(limit: int = 10, offset: int = 0, filter: str = '') -> list[Author]:
    return await crud.get_authors(limit, offset, filter)


@author.get("/{author_id}", response_model=schemas.AuthorOut, status_code=status.HTTP_200_OK)
async def get_author_data(author_id: int) -> Author:
    return await crud.get_author(author_id)


@author.put("/", status_code=status.HTTP_200_OK)
async def update_author_data(request: Request,
                             author: schemas.AuthorIn = Depends(schemas.AuthorIn.as_form),
                             profile_img: UploadFile = File(None),
                             _: int = Depends(UserWrite.super_or_admin)) -> Message:
    return await crud.update_author(author, request, profile_img)


@author.delete("/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_author(author_id: int, _: int = Depends(UserWrite.super_or_admin)) -> Response:
    return await crud.remove_author_data(author_id)
