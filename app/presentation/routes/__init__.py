from fastapi import APIRouter

from app.presentation.routes.brand_routes import router as brand_router
from app.presentation.routes.category_routes import router as category_router
from app.presentation.routes.product_routes import router as product_router
from app.presentation.routes.shopping_routes import router as shopping_router
from app.presentation.routes.supplier_routes import router as supplier_router

router = APIRouter()

router.include_router(product_router)
router.include_router(brand_router)
router.include_router(category_router)
router.include_router(supplier_router)
router.include_router(shopping_router)


# router.include_router(product_router, prefix="/api", tags=["Products"])
# router.include_router(brand_router, prefix="/api", tags=["Brands"])
