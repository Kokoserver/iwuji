from typing import List
from fastapi import APIRouter, status, Depends
from app.src.user.models import User
from app.shared.dependency import UserWrite
from app.src._base.schemas import Message
from app.src.cart import crud, schemas

cart = APIRouter()

@cart.post("/", response_model=Message, status_code=status.HTTP_201_CREATED)
async def create_cart(cart:schemas.CartIn, user:User = Depends(UserWrite.current_user_with_data)):
    return await crud.create_cart(cart, user)


@cart.put("/{id}", response_model=Message, status_code=status.HTTP_200_OK)
async def update_cart(id:int, cart:schemas.CartIn, user:User = Depends(UserWrite.current_user_with_data)):
    return await crud.update_cart(id, cart, user)

@cart.get("/", )
async def get_carts(user:User = Depends(UserWrite.current_user_with_data)):
    return await crud.get_all_cart(user)

@cart.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cart(id:int, user:User = Depends(UserWrite.current_user_with_data)):
    return await crud.delete_cart(id, user)