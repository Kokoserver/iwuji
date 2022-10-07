from datetime import datetime
from typing import List, Optional, Union
from xmlrpc.client import boolean
from app.utils.random_string import generate_pay_ref
from pydantic import BaseModel, Field, condecimal
from app.src.payment import enum
from pydantic.networks import EmailStr


class PaymentIn(BaseModel):
    orderId: str


class DataIn(BaseModel):
    link: str


class PaymentResponse(BaseModel):
    status: str
    message: str
    data: Optional[DataIn]


class Customer(BaseModel):
    order_id: str
    user_id: int
    email: EmailStr
    name: str


class VerifyPaymentResponse(BaseModel):
    tx_ref: str


class PaymentInitOut(BaseModel):
    paymentLink: str


class PaymentOut(PaymentResponse):
    status: enum.PaymentStatus = enum.PaymentStatus.PENDING
    created_at: datetime


class PaymentMeta(BaseModel):
    user_id: int
    order_id: str


class PaymentVerifyOut(BaseModel):
    error: bool
    txRef: str
    amount: int
    transactionComplete: bool


class PaymentLinkData(BaseModel):
    amount: int
    tx_ref: str
    currency: enum.PaymentCurrency = enum.PaymentCurrency.NGN
    redirect_url: str = "https://webhook.site/9d0b00ba-9a69-44fa-a43d-a82c33c36fdc"
    customer: Customer
    meta: PaymentMeta
