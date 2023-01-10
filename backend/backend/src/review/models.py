import typing as t
from backend.database.document import BaseMeta, DateMixin, Model, fields as f
from backend.src.product.models import Product
from backend.src.user.models import User


class Review(Model, DateMixin):
    class Meta(BaseMeta):
        tablename: str = "iw_review"

    comment: str = f.Text(nullable=True)
    rating: int = f.Integer(nullable=True, default=0)
    user: t.Optional[User] = f.ForeignKey(
        User,
        related_name='user_reviews',
        ondelete="CASCADE",
        onupdate="CASCADE"
    )
    product: t.Optional[Product] = f.ForeignKey(
        Product,
        related_name="product_review",
        ondelete="CASCADE",
        onupdate="CASCADE"
    )
