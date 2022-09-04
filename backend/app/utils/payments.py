
import typing as t
from app.src.order.models import OrderItem
from app.src.payment.schemas import PaymentLinkData, PaymentResponse, PaymentVerifyOut
from fastapi import status
import requests
from app.core.config import settings
payment_init_url: str = " https://api.paystack.co/transaction/initialize"
payment_verify_url: str = " https://api.paystack.co/transaction/verify/"


def generate_link(dataIn: PaymentLinkData)->PaymentResponse:
    response: requests = requests.post(url=f"{payment_init_url}", headers={
        "Authorization": f"Bearer {settings.PAYMENT_SECRET_KEY}"}, json=dataIn.dict())
    if response.status_codes == status.HTTP_200_OK:
        return PaymentResponse(**response.json())
    print(response.text)


def verify_payment(reference: str)->PaymentVerifyOut:
    response: requests = requests.post(url=f"{payment_verify_url}/{reference}", headers={
        "Authorization": f"Bearer {settings.PAYMENT_SECRET_KEY}"},)
    if response.status_codes == status.HTTP_200_OK:
        return PaymentVerifyOut(**response.json())
    print(response.text)


def get_product_total_price(items: t.List[OrderItem])->float:
    if items:
        pdf_price = 0
        hard_back_price = 0
        paper_back_price = 0
        for item in items:
            if item.pdf:
                pdf_price += item.product.property.pdf_price
            hard_back_price += item.hard_back_qty * item.product.property.hard_back_price
            paper_back_price += item.paper_back_qty * item.product.property.paper_back_price
        total_price = pdf_price + hard_back_price + paper_back_price
        return total_price