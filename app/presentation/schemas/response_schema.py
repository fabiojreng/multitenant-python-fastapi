from typing import Union

from pydantic import BaseModel


class SchemaResponseBody(BaseModel):
    type: str
    message: str | dict
    data: Union[dict, list[dict], str] | None


class SchemaResponseHttp(BaseModel):
    status_code: int
    body: SchemaResponseBody
