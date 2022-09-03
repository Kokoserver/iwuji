from datetime import datetime
from app.utils.random_string import generate_pay_ref
from pydantic import BaseModel, Field, condecimal
from app.src.payment import enum
from pydantic.networks import EmailStr


class PaymentIn(BaseModel):
    orderId: str
    pay_ref: str = Field(..., max_length=50)
    amount: condecimal(decimal_places=2, max_digits=10) = Field(...)
    currency: enum.PaymentCurrency = enum.PaymentCurrency.NGN
    method: enum.PaymentMethod = enum.PaymentMethod.CARD


class PaymentOut(PaymentIn):
    status: enum.PaymentStatus = enum.PaymentStatus.PENDING
    created_at: datetime


class PaymentMeta(BaseModel):
    consumer_id: int


class CustomerInfo(BaseModel):
    email: EmailStr
    phonenumber: str
    name: str


class PaymentCustomize(BaseModel):
    title: str
    logo: str


class paymentLink(BaseModel):
    tx_ref: str = Field(default=generate_pay_ref)
    amount: int
    currency: enum.PaymentCurrency = enum.PaymentCurrency.NGN
    redirect_url: str = "https://webhook.site/9d0b00ba-9a69-44fa-a43d-a82c33c36fdc"
    meta: PaymentMeta
    customer: CustomerInfo
    customizations: PaymentCustomize
