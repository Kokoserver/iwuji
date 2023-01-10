from typing import List
from fastapi import APIRouter, status, Depends
from backend.shared.dependency import UserWrite
from backend.src.user.models import User
from backend.src._base.schemas import Message
from backend.src.payment import schemas, crud


pay = APIRouter()


@pay.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.PaymentInitOut
)
async def create_payment_link(
    order: schemas.PaymentIn, user: User = Depends(UserWrite.current_user_with_data)
):
    return await crud.create_payment(orderIn=order, user=user)


@pay.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[schemas.PaymentDataViewOut]
)
async def get_payment_ist(user: User = Depends(UserWrite.current_user_with_data)):
    return await crud.payment_list(user=user)


@pay.post("/verify", status_code=status.HTTP_200_OK, response_model=Message)
async def verify_payment(
    data: schemas.VerifyPaymentResponse,
    user: User = Depends(UserWrite.current_user_with_data),
):
    return await crud.verify_user_payment(data=data, user=user)
