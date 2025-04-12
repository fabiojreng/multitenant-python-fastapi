from datetime import datetime, timezone
from uuid import uuid4


class StockMovement:
    def __init__(
            self,
            stock_movement_id: str,
            product_id: str,
            quantity_changed: int,
            movement_type: str,
            reason: str | None,  # Criar VO depois - Enum
            date_movement: datetime,
    ):
        self.__stock_movement_id = stock_movement_id
        self.__product_id = product_id
        self.__quantity_changed = quantity_changed
        self.__movement_type = movement_type
        self.__reason = reason
        self.__date_movement = date_movement

    @staticmethod
    def create(
            product_id: str,
            quantity_changed: int,
            movement_type: str,
            reason: str | None,
    ) -> "StockMovement":
        return StockMovement(
            str(uuid4()),
            product_id,
            quantity_changed,
            movement_type,
            reason,
            datetime.now(timezone.utc),
        )

    @staticmethod
    def restore(
            stock_movement_id: str,
            product_id: str,
            quantity_changed: int,
            movement_type: str,
            reason: str | None,
            date_movement: datetime,
    ) -> "StockMovement":
        return StockMovement(
            stock_movement_id,
            product_id,
            quantity_changed,
            movement_type,
            reason,
            date_movement,
        )

    def to_dict(self):
        return {
            "stock_movement_id": self.__stock_movement_id,
            "product_id": self.__product_id,
            "quantity_changed": self.__quantity_changed,
            "movement_type": self.__movement_type,
            "reason": self.__reason,
            "date_movement": self.__date_movement.isoformat(),
        }

    def get_stock_movement_id(self) -> str:
        return str(self.__stock_movement_id)

    def get_product_id(self) -> str:
        return str(self.__product_id)

    def get_quantity_changed(self) -> int:
        return self.__quantity_changed

    def get_movement_type(self) -> str:
        return self.__movement_type

    def get_reason(self) -> str:
        return self.__reason

    def get_date_movement(self) -> str:
        return str(self.__date_movement)
