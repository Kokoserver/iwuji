from db.model import GUID, Base, sa
from sqlalchemy.orm import relationship


class Author(Base):
    __tablename__ = "author"
    firstname = sa.Column(sa.String(20))
    lastname = sa.Column(sa.String(20))
    email = sa.Column(sa.String(50), unique=True)
    short_description = sa.Column(sa.TEXT)
    full_description = sa.Column(sa.TEXT)
    title_id = sa.Column(GUID, sa.ForeignKey("user_title.id", ondelete="SET NULL"))
    title = relationship("UserTitle", foreign_keys=[title_id])
    cover_image_id = sa.Column(GUID, sa.ForeignKey("media.id", ondelete="SET NULL"))
    cover_image = relationship("Media", foreign_keys=[cover_image_id])
