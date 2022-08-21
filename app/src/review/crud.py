from uuid import UUID
from fastapi import  status, HTTPException, Response
from app.src._base.schemas import Message
from app.src.review.models import Review
from app.src.review import schemas
from app.src.user.models import User
from app.src.product.models import Product
from tortoise.functions import  Avg


async def create_review(review:schemas.ReviewIn, user:User) -> Message:
    get_product = await Product.filter(id=review.productId).first()
    if not get_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product does not exist')
    _, created = await Review.get_or_create(**review.dict(exclude=['productId']), user=user, product=get_product)
    if created:
        return Message(message='Review created successfully')
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Review already exists')

async def update_review(id:UUID, review:schemas.ReviewIn, user:User) -> Message:
    get_product = await Product.filter(id=review.productId).first()
    if not get_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product does not exist')
    get_review = await Review.filter(product=get_product, user=user).first()
    if not get_review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Review does not exist')
    for key, value in review.dict(exclude=["productId"]).items():
        setattr(get_review, key, value)
    await get_review.save()
    return Message(message='Review updated successfully')


async def delete_review(id:UUID, user:User) -> None:
    get_review = await Review.filter(id=id, user=user).first()
    if not get_review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Review does not exist')
    await get_review.delete()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


async def get_user_review(id:UUID, user:User) -> Review:
    get_review = await Review.filter(id=id, user=user).first()
    if not get_review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Review does not exist')
    return get_review

async def get_product_review(productId:UUID, limit:int, offset:int) -> Review:
    get_review = await Review.filter(product__id=productId).all().limit(limit).offset(offset)
    if not get_review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Review does not exist')
    return get_review

async def get_product_review_count(productId:UUID) -> int:
    get_review = await Review.filter(product__id=productId).count()
    if not get_review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Review does not exist')
    return get_review

async def get_product_review_average(productId:UUID) -> float:
    get_review = await Review.filter(product__id=productId).all().annotate(Avg('rating'))
    if not get_review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Review does not exist')
    return get_review