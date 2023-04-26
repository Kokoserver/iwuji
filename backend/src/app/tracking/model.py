from db.model import GUID, Base, sa
from sqlalchemy.orm import relationship


class Tracking(Base):
    __tablename__ = "order_tracking"
    order_item_id = sa.Column(GUID, sa.ForeignKey("order_item.id", ondelete="CASCADE"))
    order_item = relationship("OrderItem", back_populates="trackings")
    location = sa.Column(sa.String(50))

    def __init__(
        self,
        order_item_id: str,
        location: str,
    ) -> None:
        self.order_item_id = order_item_id
        self.location = location
