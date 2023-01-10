from backend.src.media.models import Media
import typing as t
from backend.database.document import BaseMeta, Model, fields as f
from backend.src.author.enum import AuthorTitle


class Author(Model):
    class Meta(BaseMeta):
        tablename: str = "iw_author"
    title: str = f.String(choices=AuthorTitle, max_length=10,
                          nullable=True, default=AuthorTitle.DR)
    email: str = f.String(max_length=40)
    firstname: str = f.String(max_length=20)
    lastname: str = f.String(max_length=20)
    description: str = f.Text()
    profile_img = f.ForeignKey(
        Media,
        related_name='author_image',
        ondelete="SET NULL",
        onupdate="CASCADE")
