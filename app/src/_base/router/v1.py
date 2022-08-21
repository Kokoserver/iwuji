from fastapi import APIRouter


from app.src.auth.api.v1 import  auth
from app.src.user.api.v1 import  user
from app.src.permission.api.v1 import perm as permission
from app.src.cart.api.v1 import  cart
from app.src.product.api.v1 import product, variation
from app.src.category.api.v1 import cat as category
from app.src.order.api.v1 import order
from app.src.payment.api.v1 import pay as payment
from app.src.review.api.v1 import  review
from app.src.media.api.v1 import  media

router = APIRouter()
router.include_router(permission, prefix="/permissions", tags=["User permission"])
router.include_router(user, prefix="/users", tags=["Users"])
router.include_router(auth, prefix="/auth", tags=["Auth"])
router.include_router(cart, prefix="/carts", tags=["Carts"])
router.include_router(product, prefix="/products",  tags=["Products"])
router.include_router(variation, prefix="/variations",  tags=["Variations"])
router.include_router(category, prefix="/products/category", tags=["Product category"])
router.include_router(order, prefix="/orders", tags=["Orders"])
router.include_router(payment, prefix="/payments", tags=["Payment"])
router.include_router(review, prefix="/review", tags=["Review"])
router.include_router(media, prefix="/static", include_in_schema=False, tags=["Media_drive"])
