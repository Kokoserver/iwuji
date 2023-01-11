import logging
import typing as t
from backend.src.order.models import OrderItem
from backend.src.payment.schemas import PaymentLinkData, PaymentResponse, PaymentVerifyOut
import requests
from rave_python import Rave
from backend.core.config import settings

logging.disable(logging.NOTSET)

rave = Rave(
    publicKey=settings.RAVE_PUBLIC_KEY,
    secretKey=settings.RAVE_SECRET_KEY,
    usingEnv=False,
    production=settings.DEBUG
)
payment_init_url: str = "https://api.flutterwave.com/v3/payments"


def generate_link(dataIn: PaymentLinkData) -> PaymentResponse:
    response = requests.post(
        url=f"{payment_init_url}",
        headers={"Authorization": f"Bearer {settings.RAVE_SECRET_KEY}"},
        json=dataIn.dict(),
    )
    print(response.json())
    return PaymentResponse(**response.json())


# noinspection PyArgumentList
def verify_payment(tx_ref: str) -> PaymentVerifyOut:
    response: PaymentVerifyOut = rave.Card.verify(tx_ref)
    return PaymentVerifyOut(**response)


def get_product_total_price(items: t.List[OrderItem]) -> float:
    if items:
        pdf_price = 0
        hard_back_price = 0
        paper_back_price = 0
        for item in items:
            if item.pdf:
                pdf_price += item.product.property.pdf_price
            hard_back_price += (
                item.hard_back_qty * item.product.property.hard_back_price
            )
            paper_back_price += (
                item.paper_back_qty * item.product.property.paper_back_price
            )
        total_price = pdf_price + hard_back_price + paper_back_price
        return total_price
