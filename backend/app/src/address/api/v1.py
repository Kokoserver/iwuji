from typing import List
from fastapi import APIRouter,  Depends, status
from app.src.address import crud, schemas
from app.shared.dependency import UserWrite
from app.src.user.models import User
from app.src._base.schemas import Message


addr = APIRouter() 

@addr.post("/", status_code=status.HTTP_201_CREATED, response_model=Message)
async def create_address( address: schemas.AddressIn, user:User = Depends(UserWrite.current_user_with_data)):
    await crud.create_address(address, user)
    
@addr.get("/", response_model=List[schemas.AddressOut], status_code=status.HTTP_200_OK)
async def get_addresses(user:User = Depends(UserWrite.current_user_with_data)):
    return await crud.get_all_address(user)

@addr.get("/{address_id}", response_model=schemas.AddressOut, status_code=status.HTTP_200_OK)
async def get_address(address_id:int, user:User = Depends(UserWrite.current_user_with_data)):
    return await crud.get_address(address_id, user)

@addr.put("/{address_id}", status_code=status.HTTP_200_OK, response_model=Message)
async def update_address(address_id:int, address:schemas.AddressIn, user:User = Depends(UserWrite.current_user_with_data)):
    await crud.update_address(address_id, address, user)
    
@addr.delete("/{address_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_address(address_id:int, user:User = Depends(UserWrite.current_user_with_data))->None:
    await crud.delete_address(address_id, user)