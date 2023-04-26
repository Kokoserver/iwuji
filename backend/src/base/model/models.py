from src.app.user.model import User
from src.app.address.model import Address
from src.app.auth.model import AuthToken
from src.app.cart.model import Cart
from src.app.category.model import Category
from src.app.media_store.model import Media
from src.app.status.model import Status
from src.app.tracking.model import Tracking
from src.app.order.model import Order, OrderItem
from src.app.payment.model import Payment
from src.app.permission.model import Permission
from src.app.product.model import (
    Product,
    ProductProperty,
    ProductAttribute,
    ProductMedia,
)
from src.app.reviews.model import Review
from src.app.user_title.model import UserTitle
from src.app.author.model import Author


model_for_alembic = [
    User,
    Address,
    AuthToken,
    Cart,
    UserTitle,
    Author,
    Category,
    Media,
    Status,
    Order,
    OrderItem,
    Tracking,
    Payment,
    Permission,
    Product,
    ProductProperty,
    ProductAttribute,
    ProductMedia,
    Review,
]
