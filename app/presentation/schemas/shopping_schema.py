from pydantic import BaseModel


class ShoppingCreateSchema(BaseModel):
    supplier_id: str
    product_id: str
    price_cost: float
    quantity: int
