import uuid
from fastapi import APIRouter, Response, status
from src.app.category import schema, service


router = APIRouter(prefix="/categories", tags=["Product Category"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_category(data_in: schema.ICategoryIn) -> schema.ICategoryOut:
    return await service.create(data_in=data_in)


@router.get(
    "/{category_id}",
    response_model=schema.ICategoryOut,
    status_code=status.HTTP_200_OK,
)
async def get_category(category_id: uuid.UUID) -> schema.ICategoryOut:
    return await service.get(category_id=category_id)


@router.put(
    "/{category_id}",
    response_model=schema.ICategoryOut,
    status_code=status.HTTP_200_OK,
)
async def update_category(
    category_id: uuid.UUID, data_in: schema.ICategoryIn
) -> schema.ICategoryOut:
    return await service.update(category_id=category_id, data_in=data_in)


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(category_id: uuid.UUID) -> Response:
    return await service.delete(category_id=category_id)
