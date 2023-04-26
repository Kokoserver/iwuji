from db.model import GUID, Base, sa
from sqlalchemy.orm import relationship


class Address(Base):
    __tablename__ = "address"
    user_id = sa.Column(GUID, sa.ForeignKey("user.id", ondelete="CASCADE"))
    user = relationship("User", foreign_keys=[user_id])
    street = sa.Column(sa.String(100))
    city = sa.Column(sa.String(100))
    state = sa.Column(sa.String(100))
    postal_code = sa.Column(sa.String(10))
