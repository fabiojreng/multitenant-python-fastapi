from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy import Column, String, ForeignKey, Integer, DateTime

from app.domain.entities.stock_movements import StockMovement
from app.infra.database.base import Base


class StockMovementORM(Base):
    __tablename__ = "stock_movements"

    stock_movement_id = Column(String(36), primary_key=True, default=uuid4)
    product_id = Column(String(36), ForeignKey("products.product_id"), nullable=False)
    quantity_changed = Column(Integer, nullable=False)
    movement_type = Column(String, nullable=False)
    reason = Column(String, nullable=True)  # Converter para Enum depois
    date_movement = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    @classmethod
    def from_entity(cls, movement: "StockMovement") -> "StockMovementORM":
        return cls(
            stock_movement_id=movement.get_stock_movement_id(),
            product_id=movement.get_product_id(),
            quantity_changed=movement.get_quantity_changed(),
            movement_type=movement.get_movement_type(),
            reason=movement.get_reason(),
            date_movement=movement.get_date_movement(),
        )

    def to_entity(self) -> "StockMovement":
        return StockMovement.restore(
            stock_movement_id=self.stock_movement_id,
            product_id=self.product_id,
            quantity_changed=self.quantity_changed,
            movement_type=self.movement_type,
            reason=self.reason,
            date_movement=self.date_movement,
        )
