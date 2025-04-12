from datetime import datetime
from uuid import uuid4


class StockMovement:
    def __init__(
            self,
            stock_movement_id: str,
            product_id: str,
            quantity_changed: int,
            movement_type: int,
            reason: str | None,
            date_moviment: datetime | None
    ):
        self.__stock_movement_id = stock_movement_id
        self.__product_id = product_id
        self.__quantity_changed = quantity_changed
        self.__movement_type = movement_type
        self.__reason = reason
        self.__date_moviment = date_moviment or datetime.now()

    @staticmethod
    def create(product_id: str, quantity_changed: int, moviment_type: int, reason: str | None,
               date_moviment: str | None) -> "StockMovement":
        return StockMovement(uuid4(), product_id, quantity_changed, moviment_type, reason, date_moviment)

    @staticmethod
    def restore(stock_moviment_id: str, product_id: str, quantity_changed: int, moviment_type: int, reason: str | None,
                date_moviment: str | None) -> "StockMovement":
        return StockMovement(stock_moviment_id, product_id, quantity_changed, moviment_type, reason, date_moviment)

    def to_dict(self):
        return {
            "stock_movement_id": str(self.__stock_movement_id),
            "product_id": str(self.__product_id),
            "quantity_changed": self.__quantity_changed,
            "movement_type": self.__movement_type,
            "reason": self.__reason,
            "date_moviment": self.__date_moviment.isoformat(),
        }
