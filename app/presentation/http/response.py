from typing import Any, Union

from fastapi import status
from starlette.responses import JSONResponse

from app.presentation.schemas.response_schema import SchemaResponseHttp, SchemaResponseBody


def build_response(
        status_code: int,
        type_: str,
        message: str,
        data: Union[dict, list[dict], str] | None
) -> SchemaResponseHttp:
    return SchemaResponseHttp(
        status_code=status_code,
        body=SchemaResponseBody(
            type=type_,
            message=message,
            data=data
        )
    )


def response_ok(message: str, data: Any = None) -> SchemaResponseHttp:
    return build_response(status.HTTP_200_OK, "success", message, data)


def response_created(message: str, data: Any = None) -> SchemaResponseHttp:
    return build_response(status.HTTP_201_CREATED, "success", message, data)


def response_no_content(message: str, data: Any = None) -> SchemaResponseHttp:
    return build_response(status.HTTP_202_ACCEPTED, "success", message, data)


def response_bad_request(message: str, data: Any = None) -> SchemaResponseHttp:
    return build_response(status.HTTP_400_BAD_REQUEST, "error", message, data)


def response_conflict(message: str, data: Any = None) -> SchemaResponseHttp:
    return build_response(status.HTTP_409_CONFLICT, "error", message, data)


def response_unprocessable_entity(message: str, data: Any = None) -> SchemaResponseHttp:
    return build_response(status.HTTP_422_UNPROCESSABLE_ENTITY, "error", message, data)


def response_not_found(message: str, data: Any = None) -> SchemaResponseHttp:
    return build_response(status.HTTP_404_NOT_FOUND, "error", message, data)


def response_internal_error(message: str, data: Any = None) -> SchemaResponseHttp:
    return build_response(status.HTTP_500_INTERNAL_SERVER_ERROR, "error", message, data)


def as_json_response(schema_response: SchemaResponseHttp) -> JSONResponse:
    return JSONResponse(
        status_code=schema_response.status_code,
        content=schema_response.body.dict()
    )
