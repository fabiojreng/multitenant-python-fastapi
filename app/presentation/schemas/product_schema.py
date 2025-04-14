from pydantic import BaseModel


class ProductCreateSchema(BaseModel):
    name: str
    image: str | None
    brand_id: str
    category_id: str
    supplier_id: str
    quantity: int
    quantity_min: int | None
    price_cost: float
    selling_price: float
    validate_date: str | None


class ProductResponseSchema(ProductCreateSchema):
    product_id: str
    created_at: str
    status: str


class ProductListResponseSchema(BaseModel):
    products: list[ProductResponseSchema]
