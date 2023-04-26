from db.model import GUID, Base, sa
from sqlalchemy.orm import relationship
from src.lib.utils.random_string import generate_orderId


class Order(Base):
    __tablename__ = "order"
    order_id = sa.Column(
        sa.String(15),
        default=lambda: str(generate_orderId(15)),
        index=True,
        unique=True,
    )
    user_id = sa.Column(GUID, sa.ForeignKey("user.id", ondelete="CASCADE"))
    user = relationship("User", foreign_keys=[user_id])
    shipping_address_id = sa.Column(
        GUID, sa.ForeignKey("address.id", ondelete="SET NULL")
    )
    shipping_address = relationship("Address", foreign_keys=[shipping_address_id])
    status_id = sa.Column(
        GUID, sa.ForeignKey("status.id", ondelete="SET NULL"), nullable=True
    )
    status = relationship("Status", foreign_keys=[status_id])
    items = relationship("OrderItem", back_populates="order")


class OrderItem(Base):
    __tablename__ = "order_item"
    pdf = sa.Column(sa.Boolean, default=True)
    paper_back_qty = sa.Column(sa.Integer, default=0)
    hard_back_qty = sa.Column(sa.Integer, default=0)
    delivered = sa.Column(sa.Boolean, default=False, index=True)
    tracking_id = sa.Column(
        sa.String(10), default=lambda: str(generate_orderId(10)), index=True
    )
    trackings = relationship("Tracking", back_populates="order_item")
    product_id = sa.Column(GUID, sa.ForeignKey("product.id"))
    product = relationship("Product", foreign_keys=[product_id])
    order_id = sa.Column(GUID, sa.ForeignKey("order.id", ondelete="CASCADE"))
    order = relationship("Order", foreign_keys=[order_id])

    def __init__(
        self,
        product_id: str,
        order_id: str = None,
        pdf: bool = False,
        paper_back_qty: int = 0,
        hard_back_qty: int = 0,
        delivered: bool = False,
    ) -> None:
        self.product_id = product_id
        self.order_id = order_id
        self.pdf = pdf
        self.paper_back_qty = paper_back_qty
        self.hard_back_qty = hard_back_qty
        self.delivered = delivered
