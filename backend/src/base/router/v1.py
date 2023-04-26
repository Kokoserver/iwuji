from fastapi import APIRouter
from src.lib.utils import get_api_prefix
from src.app.user.api.v1 import router as user_api
from src.app.auth.api.v1 import router as auth_api
from src.app.product.api.v1 import router as product_api
from src.app.cart.api.v1 import router as cart_api
from src.app.address.api.v1 import router as address_api
from src.app.category.api.v1 import router as category_api
from src.app.order.api.v1 import router as order_api
from src.app.payment.api.v1 import router as payment_api
from src.app.tracking.api.v1 import router as tracking_api
from src.app.author.api.v1 import router as author_api
from src.app.reviews.api.v1 import router as review_api
from src.app.status.api.v1 import router as status_api
from src.app.user_title.api.v1 import router as title_api
from src.app.media_store.api.v1 import (
    router as media_store,
)

router = APIRouter(prefix=get_api_prefix.get_prefix())
router.include_router(title_api)
router.include_router(status_api)
router.include_router(category_api)
router.include_router(user_api)
router.include_router(auth_api)
router.include_router(author_api)
router.include_router(address_api)
router.include_router(product_api)
router.include_router(cart_api)
router.include_router(order_api)
router.include_router(payment_api)
router.include_router(tracking_api)
router.include_router(review_api)
router.include_router(media_store)
