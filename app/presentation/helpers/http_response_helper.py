from fastapi.responses import JSONResponse

from app.presentation.schemas.response_schema import SchemaResponseHttp


def http_response(response: SchemaResponseHttp) -> JSONResponse:
    return JSONResponse(
        status_code=response.status_code,
        content=response.dict()
    )
