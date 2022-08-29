from fastapi import  status, HTTPException, Response
from app.src._base.schemas import Message
from app.src.review.models import Review
from app.src.review import schemas
from app.src.user.models import User
from app.src.product.models import Product


async def create_review(review:schemas.ReviewIn, user:User) -> Message:
    get_product = await Product.objects.get_or_none(id=review.productId)
    if not get_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product does not exist')
    _, created = await Review.objects.get_or_create(**review.dict(exclude=['productId']), user=user, product=get_product)
    if created:
        return Message(message='Review created successfully')
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Review already exists')

async def update_review(id:int, review:schemas.ReviewIn, user:User) -> Message:
    get_product = await Product.objects.get_or_none(id=review.productId)
    if not get_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product does not exist')
    get_review = await Review.objects.get_or_none(product=get_product, user=user)
    if not get_review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Review does not exist')
    for key, value in review.dict(exclude=["productId"]).items():
        setattr(get_review, key, value)
    await get_review.save()
    return Message(message='Review updated successfully')


async def delete_review(id:int, user:User) -> None:
    get_review = await Review.objects.get_or_none(id=id, user=user)
    if not get_review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Review does not exist')
    await get_review.delete()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


async def get_user_review(id:int, user:User) -> Review:
    get_review = await Review.objects.get_or_none(id=id, user=user)
    if not get_review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Review does not exist')
    return get_review

async def get_product_review(productId:int, limit:int, offset:int) -> Review:
    get_review = await Review.objects.filter(product__id=productId).limit(limit).offset(offset).all()
    if not get_review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Review does not exist')
    return get_review

async def get_product_review_count(productId:int) -> int:
    get_review = await Review.objects.filter(product__id=productId).count()
    return get_review

async def get_product_review_average(productId:int) -> float:
    get_review = await Review.objects.filter(product__id=productId).avg('rating')
    if not get_review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Review does not exist')
    return get_review