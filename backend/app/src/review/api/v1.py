from typing import List
from uuid import UUID
from fastapi import APIRouter, status, Depends
from ....shared.dependency import UserWrite
from app.src._base.schemas import Message
from app.src.review import crud, schemas
from app.src.user.models import User


review = APIRouter()


@review.post("/", response_model=Message, status_code=status.HTTP_201_CREATED)
async def create_review(review: schemas.ReviewIn, user: User = Depends(UserWrite.current_user_with_data)):
    return await crud.create_review(review, user)


@review.get("/", response_model=List[schemas.ReviewIn], status_code=status.HTTP_200_OK)
async def get_reviews(filter: str = '', limit: int = 10, offset: int = 0):
    return await crud.get_reviews(filter, limit, offset)


@review.put("/{id}", response_model=Message, status_code=status.HTTP_200_OK)
async def update_review(id: int, review: schemas.ReviewIn, user: User = Depends(UserWrite.current_user_with_data)):
    return await crud.update_review(id, review, user)


@review.get("/{id}", response_model=schemas.ReviewOut)
async def get_user_review(id: int, user: User = Depends(UserWrite.current_user_with_data)):
    return await crud.get_user_review(id, user)


@review.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_review(id: int, user: User = Depends(UserWrite.current_user_with_data)):
    return await crud.delete_review(id, user)


@review.get("/product/{productId}", response_model=List[schemas.ReviewOut])
async def get_product_review(productId: int, limit: int = 10, offset: int = 0):
    return await crud.get_product_review(productId, limit, offset)


@review.get("/product/{productId}/count", response_model=int)
async def get_product_review_count(productId: int):
    return await crud.get_product_review_count(productId)


@review.get("/product/{productId}/rating", response_model=int)
async def get_product_review_average(productId: int):
    return await crud.get_product_review_average(productId)
