import typing as t
from backend.database.document import BaseMeta, Model, DateMixin, fields as f

from backend.src.product.models import Product
from backend.src.user.models import User


class Cart(Model, DateMixin):
    """_summary_ = "Cart"
      description = "Cart model for keeping all the cart details"
   """

    class Meta(BaseMeta):
        tablename: str = "iw_cart"

    pdf: bool = f.Boolean(default=False)
    paper_back_qty: int = f.Integer(default=0)
    hard_back_qty: int = f.Integer(default=0)
    product: t.Optional[Product] = f.ForeignKey(
        Product,
        related_name="cart_product",
        ondelete="CASCADE",
        onupdate="CASCADE"
    )
    user: t.Optional[User] = f.ForeignKey(
        User,
        related_name="user_cart",
        ondelete="CASCADE",
        onupdate="CASCADE"
    )
