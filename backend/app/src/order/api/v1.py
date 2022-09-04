from fastapi import APIRouter, status, Depends
from app.shared.dependency import UserWrite
from app.src.user.models import User
from app.src._base.schemas import Message
from app.src.order import schemas, crud


order = APIRouter()


@order.post("/", status_code=status.HTTP_201_CREATED, response_model=str)
async def create_order(data: schemas.OrderIn, user: User = Depends(UserWrite.current_user_with_data)):
    return await crud.create_order(data=data, user=user)


@order.get("/")
async def get_all_orders(filter: str, limit: int = 10, offset: int = 0, user: User = Depends(UserWrite.current_user_with_data)):
    return await crud.get_all_orders(filter=filter, limit=limit, offset=offset, user=user)


@order.get("/{orderId}")
async def get_order(orderId: str, user: User = Depends(UserWrite.current_user_with_data)):
    return await crud.get_order(orderId=orderId, user=user)


@order.delete("/{orderId}")
async def delete_order(orderId: str, user: User = Depends(UserWrite.current_user_with_data)):
    await crud.delete_order(user=user, orderId=orderId)