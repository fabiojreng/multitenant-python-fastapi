from datetime import datetime, timezone
from uuid import uuid4

from app.domain.value_objects.price import Price


class ProductPriceHistory:
    def __init__(
            self,
            product_price_history_id: str,
            product_id: str,
            price_type: str,
            price: Price,
            created_at: datetime,
    ):
        self.__product_price_history_id = product_price_history_id
        self.__product_id = product_id
        self.__price_type = price_type
        self.__price = price
        self.__created_at = created_at

    @staticmethod
    def create(
            product_id: str,
            price_type: str,
            price: Price,
    ) -> "ProductPriceHistory":
        return ProductPriceHistory(
            uuid4(),
            product_id,
            price_type,
            Price(price),
            datetime.now(timezone.utc),
        )

    @staticmethod
    def restore(
            product_price_history_id: str,
            product_id: str,
            price_type: str,
            price: Price,
            created_at: datetime,
    ) -> "ProductPriceHistory":
        return ProductPriceHistory(
            product_price_history_id,
            product_id,
            price_type,
            Price(price),
            created_at,
        )

    def to_dict(self):
        return {
            "product_price_history_id": self.__product_price_history_id,
            "product_id": self.__product_id,
            "price_type": self.__price_type,
            "price": self.__price.get_value(),
            "created_at": self.__created_at.isoformat(),
        }
