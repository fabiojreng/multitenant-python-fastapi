from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from app.presentation.exceptions.handlers import validation_exception_handler
from app.presentation.middleware.tenant_manager import TenantMiddleware
from app.presentation.routes import router

app = FastAPI()

app.add_middleware(TenantMiddleware)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

app.include_router(router)
