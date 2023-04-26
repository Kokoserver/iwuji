from db.model import Base, sa


class Status(Base):
    __tablename__ = "status"
    name = sa.Column(sa.String(24))

    def __init__(self, name: str):
        self.name = name
