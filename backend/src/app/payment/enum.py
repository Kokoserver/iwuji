from enum import Enum


class PaymentMethod(str, Enum):
    CARD = "card"
    BANK = "bank"
    ADDRESS = "address"


class PaymentCurrency(str, Enum):
    NGN = "NGN"
    USD = "USD"
