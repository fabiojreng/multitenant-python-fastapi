from pydantic import BaseModel


class SupplierCreateSchema(BaseModel):
    cod: int | None
    name: str
    document: str | None
    email: str
    phone: str | None


class SupplierResponseSchema(SupplierCreateSchema):
    supplier_id: str
    created_at: str
