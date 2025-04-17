from fastapi import APIRouter

from app.presentation.routes.brand_routes import router as brand_router
from app.presentation.routes.product_routes import router as product_router

router = APIRouter()

router.include_router(product_router)
router.include_router(brand_router)

# router.include_router(product_router, prefix="/api", tags=["Products"])
# router.include_router(brand_router, prefix="/api", tags=["Brands"])
