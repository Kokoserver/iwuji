import uuid
from fastapi import APIRouter, Response, status
from src.app.user_title import schema, service


router = APIRouter(prefix="/titles", tags=["User titles"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_title(data_in: schema.ITitleIn) -> schema.ITitleOut:
    return await service.create(data_in=data_in)


@router.get(
    "/{title_id}",
    response_model=schema.ITitleOut,
    status_code=status.HTTP_200_OK,
)
async def get_title(title_id: uuid.UUID) -> schema.ITitleOut:
    return await service.get(title_id=title_id)


@router.put(
    "/{title_id}",
    response_model=schema.ITitleOut,
    status_code=status.HTTP_200_OK,
)
async def update_title(
    title_id: uuid.UUID, data_in: schema.ITitleIn
) -> schema.ITitleOut:
    return await service.update(title_id=title_id, data_in=data_in)


@router.delete("/{title_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_title(title_id: uuid.UUID) -> Response:
    return await service.delete(title_id=title_id)
