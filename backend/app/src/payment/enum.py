from enum import Enum


class PaymentStatus(str, Enum):
    SUCCESS = "success"
    PENDING = "pending"
    FAIL = "fail"


class PaymentMethod(str, Enum):
    CARD = "card"
    BANK = "bank"
    ADDRESS = "address"


class PaymentCurrency(str, Enum):
    NGN = "NGN"
    USD = "USD"
