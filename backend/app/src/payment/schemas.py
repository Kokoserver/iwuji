from datetime import datetime
from typing import List
from xmlrpc.client import boolean
from app.utils.random_string import generate_pay_ref
from pydantic import BaseModel, Field, condecimal
from app.src.payment import enum
from pydantic.networks import EmailStr


class DataIn(BaseModel):
    authorization_url: str
    access_code: str
    reference: str


class PaymentResponse(BaseModel):
    status: bool
    message: str
    data: DataIn


class VerifyData(BaseModel):
    status: str
    reference: str
    amount: int
    channel: str
    currency: str


class PaymentVerifyOut(BaseModel):
    data: VerifyData


class VerifyPaymentResponse(BaseModel):
    reference: str
    orderId: str


class PaymentOut(PaymentResponse):
    status: enum.PaymentStatus = enum.PaymentStatus.PENDING
    created_at: datetime


class PaymentMeta(BaseModel):
    user_id: int
    order_id: int
    cancel_action: str


class PaymentLinkData(BaseModel):
    amount: int
    email: EmailStr
    reference: str = Field(default=generate_pay_ref)
    channel: List[str] = ["card", "bank", "ussd"]
    currency: enum.PaymentCurrency = enum.PaymentCurrency.NGN
    callback_url: str = "https://webhook.site/9d0b00ba-9a69-44fa-a43d-a82c33c36fdc"
    metadata: PaymentMeta
