import typing as t
from backend.database.document import BaseMeta, DateMixin, Model, fields as f
from pydantic import condecimal as dc
from backend.src.order.models import Order
from backend.src.payment.enum import PaymentStatus, PaymentMethod, PaymentCurrency
from backend.src.user.models import User


class Payment(Model, DateMixin):
    """_summary_ = "Payment"
    description = "Payment model for keeping all the payments of the user"
    """

    class Meta(BaseMeta):
        tablename: str = "iw_payment"

    pay_ref: str = f.String(max_length=20, index=True, unique=True)
    amount: dc(max_digits=10, decimal_places=2) = f.Decimal(
        max_digits=10, decimal_places=2, nullable=True
    )
    currency: PaymentCurrency = f.String(
        max_length=20, choices=list(PaymentCurrency), default=PaymentCurrency.NGN
    )
    method: PaymentMethod = f.String(
        max_length=20, choices=list(PaymentMethod), default=PaymentMethod.CARD
    )
    status: PaymentStatus = f.String(
        max_length=20, choices=list(PaymentStatus), default=PaymentStatus.PENDING
    )
    order: t.Optional[Order] = f.ForeignKey(
        Order, related_name="order_payment", ondelete="CASCADE", onupdate="CASCADE"
    )
    user: t.Optional[User] = f.ForeignKey(
        User, related_name="user_payment", ondelete="CASCADE", onupdate="CASCADE"
    )
