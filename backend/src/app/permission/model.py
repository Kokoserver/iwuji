from db.model import Base, sa


class Permission(Base):
    __tablename__ = "permission"
    name = sa.Column(sa.String(24))

    def __init__(self, name: str) -> None:
        self.name = name
