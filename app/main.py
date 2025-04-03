from fastapi import FastAPI

from app.presentation.middleware.tenant_manager import TenantMiddleware
from app.presentation.routes import router

app = FastAPI()

app.add_middleware(TenantMiddleware)

app.include_router(router)
