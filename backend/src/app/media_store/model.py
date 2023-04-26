from db.model import Base, sa


class Media(Base):
    __tablename__ = "media"
    name = sa.Column(sa.String, nullable=False)
    alt = sa.Column(sa.String, unique=True, index=True)
    url = sa.Column(sa.String, unique=True)
    content_type = sa.Column(sa.String(30))
    is_active = sa.Column(sa.Boolean, default=True)
