from db.model import GUID, Base, sa
from sqlalchemy.orm import relationship


class Cart(Base):
    __tablename__ = "cart"
    pdf = sa.Column(sa.Boolean, default=True)
    paper_back_qty = sa.Column(sa.Integer, default=0)
    hard_back_qty = sa.Column(sa.Integer, default=0)
    item_id = sa.Column(GUID, sa.ForeignKey("product.id", ondelete="SET NULL"), nullable=False)
    item = relationship("Product", foreign_keys=[item_id])
    user_id = sa.Column(GUID, sa.ForeignKey("user.id", ondelete="CASCADE"))
    user = relationship("User", foreign_keys=[user_id])
