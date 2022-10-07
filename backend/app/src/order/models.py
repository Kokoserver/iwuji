import typing as t
from app.database.document import BaseMeta, DateMixin, Model, fields as f
from app.src.address.models import ShippingAddress
from app.src.product.models import Product
from app.src.order.enum import OrderStatus
from app.src.user.models import User
from app.utils.random_string import generate_orderId


class Order(Model, DateMixin):
    """_summary_ = "Order"
    description = "Order model for keeping all the orders of the user"
    """

    class Meta(BaseMeta):
        tablename: str = "iw_order"

    orderId: t.Optional[str] = f.String(
        max_length=15, default=generate_orderId, index=True, unique=True
    )
    user: t.Optional[User] = f.ForeignKey(
        User, related_name="user_order", ondelete="CASCADE", onupdate="CASCADE"
    )
    shipping_address: t.Optional[ShippingAddress] = f.ForeignKey(
        ShippingAddress,
        related_name="order_address",
        ondelete="SET NULL",
        nullable=True,
    )
    status: OrderStatus = f.String(
        choices=list(OrderStatus), default=OrderStatus.PENDING, max_length=20
    )


class OrderItem(Model):
    class Meta(BaseMeta):
        pass

    pdf: bool = f.Boolean(default=False)
    paper_back_qty = f.Integer(default=0)
    hard_back_qty = f.Integer(default=0)
    product: t.Optional[Product] = f.ForeignKey(
        Product,
        related_name="order_item_product",
        ondelete="CASCADE",
        onupdate="CASCADE",
    )
    order: t.Optional[Order] = f.ForeignKey(
        Order, related_name="order_item_order", ondelete="CASCADE", onupdate="CASCADE"
    )
    deliver: bool = f.Boolean(default=False)
