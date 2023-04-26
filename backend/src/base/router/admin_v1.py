from fastapi import APIRouter

# , Depends
from src.lib.utils import get_api_prefix

# from src.lib.shared.dependency import UserWrite
from src.app.user.api.admin_v1 import router as user_api
from src.app.category.api.admin_v1 import router as category_api
from src.app.permission.api.v1 import router as permission_api
from src.app.product.api.admin_v1 import router as product_api
from src.app.order.api.admin_v1 import router as order_api
from src.app.payment.api.admin_v1 import router as payment_api
from src.app.reviews.api.admin_v1 import router as review_api
from src.app.product.api.admin_v1 import variation as variation_api
from src.app.status.api.admin_v1 import router as status_api
from src.app.user_title.api.admin_v1 import router as title_api
from src.app.tracking.api.admin_v1 import router as tracking_api
from src.app.author.api.admin_v1 import router as author_api

router = APIRouter(prefix=f"{get_api_prefix.get_prefix()}")
router.include_router(
    router=permission_api,

    #     dependencies=[Depends(UserWrite.super_or_admin)],
)
router.include_router(
    router=user_api,
    #       dependencies=[Depends(UserWrite.is_super_admin)]
)

router.include_router(
    router=category_api,
    # dependencies=[Depends(UserWrite.super_or_admin)]
)

router.include_router(
    router=product_api,
    #     dependencies=[Depends(UserWrite.super_or_admin)],
)
router.include_router(
    router=payment_api,
    #     dependencies=[Depends(UserWrite.super_or_admin)],
)
router.include_router(
    router=order_api,
    #     dependencies=[Depends(UserWrite.super_or_admin)],
)
router.include_router(
    router=variation_api,
    #     dependencies=[Depends(UserWrite.super_or_admin)],
)
router.include_router(
    router=review_api,
    #     dependencies=[Depends(UserWrite.super_or_admin)],
)
router.include_router(
    router=status_api,
    #     dependencies=[Depends(UserWrite.super_or_admin)],
)
router.include_router(
    router=title_api,
    #     dependencies=[Depends(UserWrite.super_or_admin)],
)
router.include_router(
    router=tracking_api,
    #     dependencies=[Depends(UserWrite.super_or_admin)],
)
router.include_router(
    router=author_api,
    #     dependencies=[Depends(UserWrite.super_or_admin)],
)
