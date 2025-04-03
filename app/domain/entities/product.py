from datetime import datetime, timezone, date
from typing import Optional
from uuid import uuid4

from app.domain.value_objects.price import Price
from app.domain.value_objects.status import ProductStatus


class Product:
    def __init__(
            self,
            product_id: str,
            name: str,
            brand_id: str | None,
            category_id: str | None,
            supplier_id: str,
            quantity: int,
            price_cost: Price,
            selling_price: Price,
            created_at: datetime,
            status: ProductStatus,
            image: Optional[str] = None,
            quantity_min: Optional[int] = None,
            validate_date: Optional[date] = None,
    ):
        self.__product_id = product_id
        self.__name = name
        self.__image = image
        self.__brand_id = brand_id
        self.__category_id = category_id
        self.__supplier_id = supplier_id
        self.__quantity = quantity
        self.__quantity_min = quantity_min
        self.__price_cost = price_cost
        self.__selling_price = selling_price
        self.__validate_date = validate_date
        self.__created_at = created_at
        self.__status = status

    @staticmethod
    def create(
            name: str,
            image: str | None,
            brand_id: str | None,
            category_id: str | None,
            supplier_id: str,
            quantity: int,
            price_cost: float,
            selling_price: float,
            quantity_min: Optional[int] = None,
            validate_date: Optional[date] = None,
    ) -> "Product":
        return Product(
            uuid4(),
            name,
            brand_id,
            category_id,
            supplier_id,
            quantity,
            Price(price_cost),
            Price(selling_price),
            datetime.now(timezone.utc),
            ProductStatus.ACTIVE,
            image,
            quantity_min,
            validate_date,
        )

    @staticmethod
    def restore(
            product_id: str,
            name: str,
            quantity: int,
            price_cost: float,
            selling_price: float,
            created_at: datetime,
            status: str,
            brand_id: str | None,
            category_id: str | None,
            supplier_id: str,
            image: Optional[str] = None,
            quantity_min: Optional[int] = None,
            validate_date: Optional[date] = None,
    ) -> "Product":
        return Product(
            product_id,
            name,
            brand_id,
            category_id,
            supplier_id,
            quantity,
            Price(price_cost),
            Price(selling_price),
            created_at,
            ProductStatus(status),
            image,
            quantity_min,
            validate_date,
        )

    def to_dict(self) -> dict:
        return {
            "product_id": str(self.__product_id),
            "name": self.__name,
            "brand_id": self.__brand_id,
            "category_id": self.__category_id,
            "supplier_id": self.__supplier_id,
            "quantity": self.__quantity,
            "quantity_min": self.__quantity_min,
            "price_cost": self.__price_cost.get_value(),
            "selling_price": self.__selling_price.get_value(),
            "validate_date": (
                self.__validate_date.isoformat() if self.__validate_date else None
            ),
            "created_at": self.__created_at,
            "status": self.__status.value,
            "image": self.__image,
        }
