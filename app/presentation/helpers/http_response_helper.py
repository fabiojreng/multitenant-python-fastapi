from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.presentation.schemas.response_schema import SchemaResponseHttp


def http_response(response: SchemaResponseHttp):
    return JSONResponse(
        status_code=response.status_code,
        content=jsonable_encoder(response)
    )
