from typing import List
from fastapi import APIRouter, status
from app.src._base.schemas import Message

from app.src.category import crud, schemas
from app.src.category import schemas
cat = APIRouter()


@cat.post("/", status_code=status.HTTP_201_CREATED)
async def create_category(new_data: schemas.CategoryIn)->Message:
    return await crud.create_category(new_data)


@cat.get("/", response_model=List[schemas.CategoryOut], status_code=status.HTTP_200_OK)
async def get_all_categories(limit: int = 10, offset: int = 0, filter: str = '')->List[schemas.CategoryOut]:
    return await crud.get_all_categories(limit=limit, offset=offset, filter=filter)

@cat.get("/{id}", response_model=schemas.CategoryOut, status_code=status.HTTP_200_OK)
async def get_category(id:int)->schemas.CategoryOut:
    return await crud.get_category(id)

@cat.put("/{id}", response_model=Message, status_code=status.HTTP_200_OK)
async def update_category(id:int, new_data: schemas.CategoryIn)->Message:
    return await crud.update_category(id, new_data)

@cat.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(id:int)->None:
    return await crud.delete_category(id)