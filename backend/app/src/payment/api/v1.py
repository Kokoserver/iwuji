from fastapi import APIRouter, status, Depends
from app.shared.dependency import UserWrite
from app.src.user.models import User
from app.src._base.schemas import Message
from app.src.payment import schemas, crud


pay = APIRouter()


@pay.post("/{orderId}", status_code=status.HTTP_201_CREATED, response_model=schemas.PaymentResponse)
async def create_payment_link(orderId: str, user: User = Depends(UserWrite.current_user_with_data)):
    return await crud.create_payment(orderId=orderId, user=user)


@pay.post("/verify", status_code=status.HTTP_200_OK, response_model=Message)
async def verify_payment(data: schemas.VerifyPaymentResponse, user: User = Depends(UserWrite.current_user_with_data)):
    return await crud.verify_user_payment(data=data, user=user)