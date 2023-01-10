from fastapi import APIRouter


from backend.src.auth.api.v1 import auth
from backend.src.user.api.v1 import user
from backend.src.author.api.v1 import author
from backend.src.permission.api.v1 import perm as permission
from backend.src.cart.api.v1 import cart
from backend.src.product.api.v1 import product, variation
from backend.src.category.api.v1 import cat as category
from backend.src.order.api.v1 import order
from backend.src.payment.api.v1 import pay as payment
from backend.src.review.api.v1 import review
from backend.src.media.api.v1 import media
from backend.src.address.api.v1 import addr

router = APIRouter()
router.include_router(permission, prefix="/permissions", tags=["User permission"])
router.include_router(user, prefix="/users", tags=["Users"])
router.include_router(auth, prefix="/auth", tags=["Auth"])
router.include_router(author, prefix="/authors", tags=["Author"])
router.include_router(addr, prefix="/address", tags=["Shipping Address"])
router.include_router(cart, prefix="/carts", tags=["Carts"])
router.include_router(product, prefix="/products", tags=["Products"])
router.include_router(variation, prefix="/variations", tags=["Variations"])
router.include_router(category, prefix="/products/category", tags=["Product category"])
router.include_router(order, prefix="/orders", tags=["Orders"])
router.include_router(payment, prefix="/payments", tags=["Payment"])
router.include_router(review, prefix="/reviews", tags=["Review"])
router.include_router(media, prefix="/static",
                      include_in_schema=True, tags=["Media_drive"])
