from typing import List
from fastapi import APIRouter, status, Depends
from app.src.user.models import User
from app.shared.dependency import UserWrite
from app.src._base.schemas import Message
from app.src.cart import crud, schemas

cart = APIRouter()


@cart.post("/", response_model=Message, status_code=status.HTTP_201_CREATED)
async def create_cart(cart: schemas.CartIn, user: User = Depends(UserWrite.current_user_with_data)):
    return await crud.create_cart(cart, user)


@cart.put("/", response_model=schemas.CartOut, status_code=status.HTTP_200_OK)
async def update_cart(cart: schemas.CartUpdateIn, user: User = Depends(UserWrite.current_user_with_data)):
    return await crud.update_cart(cart, user)


@cart.get("/", response_model=List[schemas.CartOut])
async def get_carts(user: User = Depends(UserWrite.current_user_with_data)):
    return await crud.get_all_cart(user)


@cart.get("/{cartId}", response_model=schemas.CartOut, status_code=status.HTTP_200_OK)
async def get_cart(cartId: int, user: User = Depends(UserWrite.current_user_with_data))->schemas.CartOut:
    return await crud.get_cart(cartId, user)


@cart.delete("/{cartId}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cart(cartId: int, user: User = Depends(UserWrite.current_user_with_data)):
    return await crud.delete_cart(cartId, user)