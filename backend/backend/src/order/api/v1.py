from typing import List
from fastapi import APIRouter, status, Depends
from backend.shared.dependency import UserWrite
from backend.src.user.models import User

from backend.src.order import schemas, crud


order = APIRouter()


@order.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.OrderOut)
async def create_order(
    data: schemas.OrderIn, user: User = Depends(UserWrite.current_user_with_data)
):
    return await crud.create_order(data=data, user=user)


@order.get(
    "/", response_model=List[schemas.OrderListOut], status_code=status.HTTP_200_OK
)
async def get_all_orders(
    filter: str = "",
    limit: int = 10,
    offset: int = 0,
    user: User = Depends(UserWrite.current_user_with_data),
):
    return await crud.get_all_orders(
        filter=filter, limit=limit, offset=offset, user=user
    )


@order.get("/{orderId}", response_model=schemas.OrderDetailsOut)
async def get_order(
    orderId: str, user: User = Depends(UserWrite.current_user_with_data)
):
    return await crud.get_order(orderId=orderId, user=user)


@order.delete("/{orderId}")
async def delete_order(
    orderId: str, user: User = Depends(UserWrite.current_user_with_data)
):
    await crud.delete_order(user=user, orderId=orderId)
