from datetime import datetime
from uuid import uuid4


class Shopping:
    def __init__(
            self,
            shopping_id: str,
            supplier_id: str,
            product_id: str,
            price_cost: float,
            quantity: int,
            created_at: datetime
    ):
        self.__shopping_id = shopping_id
        self.__supplier_id = supplier_id
        self.__product_id = product_id
        self.__price_cost = price_cost
        self.__quantity = quantity
        self.__created_at = created_at

    @staticmethod
    def create(supplier_id: str, product_id: str, price_cost: float, quantity: int) -> "Shopping":
        return Shopping(str(uuid4()), supplier_id, product_id, price_cost, quantity, datetime.utcnow())

    @staticmethod
    def restore(
            shopping_id: str,
            supplier_id: str,
            product_id: str,
            price_cost: float,
            quantity: int,
            created_at: datetime
    ) -> "Shopping":
        return Shopping(shopping_id, supplier_id, product_id, price_cost, quantity, created_at)

    def to_dict(self):
        return {
            "shopping_id": self.__shopping_id,
            "supplier_id": self.__supplier_id,
            "product_id": self.__product_id,
            "price_cost": self.__price_cost,
            "quantity": self.__quantity,
            "created_at": self.__created_at.isoformat()
        }

    def get_shopping_id(self):
        return self.__shopping_id

    def get_supplier_id(self):
        return self.__supplier_id

    def get_product_id(self):
        return self.__product_id

    def get_price_cost(self):
        return self.__price_cost

    def get_quantity(self):
        return self.__quantity

    def get_created_at(self):
        return self.__created_at
