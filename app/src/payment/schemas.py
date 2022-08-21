from datetime import datetime
from pydantic import BaseModel, Field, condecimal
from app.src.payment import enum


class PaymentIn(BaseModel):
    orderId: str
    pay_ref: str = Field(..., max_length=50)
    amount:condecimal(decimal_places=2, max_digits=5) = Field(...)
    currency:enum.PaymentCurrency = enum.PaymentCurrency.NGN
    method:enum.PaymentMethod = enum.PaymentMethod.CARD

class PaymentOut(PaymentIn):
    status:enum.PaymentStatus = enum.PaymentStatus.PENDING
    created_at:datetime