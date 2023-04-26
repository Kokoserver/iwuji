from db.model import GUID, Base, sa
from sqlalchemy.orm import relationship
from src.lib.utils.random_string import generate_orderId


class Payment(Base):
    __tablename__ = "payments"
    reference = sa.Column(sa.String(15), default=lambda: generate_orderId(15))
    total_payed = sa.Column(sa.Numeric(precision=10, scale=2))
    completed = sa.Column(sa.Boolean, default=False)
    order_id = sa.Column(GUID, sa.ForeignKey("order.id", ondelete="CASCADE"))
    order = relationship("Order", foreign_keys=[order_id], uselist=False)

    def __init__(
        self,
        order_id: str,
        total_payed: float,
        completed: bool = False,
        reference: str = None,
    ):
        self.reference = reference
        self.total_payed = total_payed
        self.completed = completed
        self.order_id = order_id
