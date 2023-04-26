from db.model import Base, sa


class UserTitle(Base):
    __tablename__ = "user_title"
    name = sa.Column(sa.String(24))

    def __init__(self, name: str):
        self.name = name
