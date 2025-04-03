from uuid import uuid4
from datetime import datetime, date, timezone
from typing import Optional


class StockMovement:
    def __init__(
        self,
        stock_movement_id: str,
        product_id: str,
        quantity_changed: int,
        movement_type: int,
        # date_moviment: date,
        reason: Optional[str],
        created_at: datetime,
    ):
        self.__stock_movement_id = stock_movement_id
        self.__product_id = product_id
        self.__quantity_changed = quantity_changed
        self.__movement_type = movement_type
        # self.__date_moviment = date_moviment
        self.__reason = reason
        self.__created_at = created_at

    @staticmethod
    def create(
        product_id: str,
        quantity_changed: int,
        movement_type: int,
        date_moviment: date,
        reason: Optional[str] = None,
    ) -> "StockMovement":
        return StockMovement(
            str(uuid4()),
            product_id,
            quantity_changed,
            movement_type,
            date_moviment,
            reason,
            datetime.now(timezone.utc),
        )

    @staticmethod
    def restore(
        stock_movement_id: str,
        product_id: str,
        quantity_changed: int,
        movement_type: int,
        date_moviment: date,
        reason: Optional[str],
        created_at: datetime,
    ) -> "StockMovement":
        return StockMovement(
            stock_movement_id,
            product_id,
            quantity_changed,
            movement_type,
            date_moviment,
            reason,
            created_at,
        )

    def to_dict(self):
        return {
            "stock_movement_id": self.__stock_movement_id,
            "product_id": self.__product_id,
            "quantity_changed": self.__quantity_changed,
            "movement_type": self.__movement_type,
            "date_moviment": self.__date_moviment.isoformat(),
            "reason": self.__reason,
            "created_at": self.__created_at.isoformat(),
        }
