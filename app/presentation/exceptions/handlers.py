from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.presentation.http.response import response_unprocessable_entity


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content=response_unprocessable_entity(
            message="Erro de validação",
            data=exc.errors()
        ).dict()
    )
