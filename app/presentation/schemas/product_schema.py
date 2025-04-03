from datetime import datetime

from pydantic import BaseModel

from app.domain.value_objects.status import ProductStatus


class ProductCreateSchema(BaseModel):
    name: str
    # image: str | None
    # brand_id: str
    # category_id: str
    # supplier_id: str
    # quantity: int
    # quantity_min: int | None
    # price_cost: float
    # selling_price: float
    # validate_date: date | None


class ProductResponseSchema(ProductCreateSchema):
    product_id: str
    created_at: datetime
    status: ProductStatus
