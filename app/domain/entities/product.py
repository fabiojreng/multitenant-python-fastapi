from datetime import datetime, timezone, date
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
            image: str | None,
            quantity_min: str | None,
            validate_date: str | None,
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
            quantity_min: int = None,
            validate_date: date = None,
    ) -> "Product":
        return Product(
            str(uuid4()),
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
            image: str = None,
            quantity_min: int = None,
            validate_date: date = None,
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
            "product_id": self.__product_id,
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

    def get_product_id(self) -> str:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def get_image(self) -> str | None:
        return self.__image

    def get_brand_id(self) -> str | None:
        return self.__brand_id

    def get_category_id(self) -> str | None:
        return self.__category_id

    def get_supplier_id(self) -> str:
        return self.__supplier_id

    def get_quantity(self) -> int:
        return self.__quantity

    def get_quantity_min(self) -> int | None:
        return self.__quantity_min

    def get_price_cost(self) -> float:
        return self.__price_cost.get_value()

    def get_selling_price(self) -> float:
        return self.__selling_price.get_value()

    def get_validate_date(self) -> str | None:
        return self.__validate_date

    def get_created_at(self) -> str:
        return str(self.__created_at)

    def get_status(self) -> str:
        return self.__status.value
