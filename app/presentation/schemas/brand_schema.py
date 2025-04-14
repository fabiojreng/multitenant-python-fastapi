from pydantic import BaseModel


class BrandCreateSchema(BaseModel):
    name: str
    description: str


class BrandResponseSchema(BrandCreateSchema):
    brand_id: str
    created_at: str
