from typing import List
from fastapi import APIRouter, status
from backend.src._base.schemas import Message

from backend.src.category import crud, schemas
from backend.src.category import schemas
from backend.src.category.models import Category

cat = APIRouter()


@cat.post("/", status_code=status.HTTP_201_CREATED)
async def create_category(new_data: schemas.CategoryIn) -> Message:
    return await crud.create_category(new_data)


@cat.get("/", response_model=List[schemas.CategoryOut], status_code=status.HTTP_200_OK)
async def get_all_categories(limit: int = 10, offset: int = 0, filter: str = '') -> list[Category]:
    return await crud.get_all_categories(limit=limit, offset=offset, filter=filter)


@cat.get("/{user_id}", response_model=schemas.CategoryOut, status_code=status.HTTP_200_OK)
async def get_category(id: int) -> Category:
    return await crud.get_category(id)


@cat.put("/{user_id}", response_model=Message, status_code=status.HTTP_200_OK)
async def update_category(id: int, new_data: schemas.CategoryIn) -> Category:
    return await crud.update_category(id, new_data)


@cat.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(id: int) -> None:
    return await crud.delete_category(id)
