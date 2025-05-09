from pydantic import BaseModel


class BrandCreateSchema(BaseModel):
    name: str
    description: str | None


class BrandResponseSchema(BrandCreateSchema):
    brand_id: str
    created_at: str


class BrandListResponseSchema(BaseModel):
    brands: list[BrandResponseSchema]
