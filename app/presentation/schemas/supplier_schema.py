from datetime import datetime

from pydantic import BaseModel


class SupplierCreateSchema(BaseModel):
    cod: int
    name: str
    document: str
    email: str
    phone: str


class SupplierResponseSchema(SupplierCreateSchema):
    supplier_id: str
    created_at: datetime
