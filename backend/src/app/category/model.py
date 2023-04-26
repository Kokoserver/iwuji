from db.model import Base, sa


class Category(Base):
    __tablename__ = "category"
    name = sa.Column(sa.String(24))

    def __init__(self, name: str):
        self.name = name
