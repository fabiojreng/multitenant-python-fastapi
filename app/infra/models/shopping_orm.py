from datetime import datetime, timezone

from sqlalchemy import Column, String, ForeignKey, Numeric, Integer, DateTime
from sqlalchemy.orm import relationship

from app.domain.entities.shopping import Shopping
from app.infra.database.base import Base


class ShoppingORM(Base):
    __tablename__ = "shopping"

    shopping_id = Column(String(36), primary_key=True)
    supplier_id = Column(String(36), ForeignKey("suppliers.supplier_id"), nullable=False)
    product_id = Column(String(36), ForeignKey("products.product_id"), nullable=False)
    price_cost = Column(Numeric(10, 2), nullable=False)
    quantity = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    product = relationship("ProductORM", back_populates="shoppings")

    @classmethod
    def from_entity(cls, shopping: Shopping) -> "ShoppingORM":
        return cls(
            shopping_id=shopping.get_shopping_id(),
            supplier_id=shopping.get_supplier_id(),
            product_id=shopping.get_product_id(),
            price_cost=shopping.get_price_cost(),
            quantity=shopping.get_quantity(),
            created_at=shopping.get_created_at()
        )

    def to_entity(self) -> Shopping:
        return Shopping.restore(
            shopping_id=self.shopping_id,
            supplier_id=self.supplier_id,
            product_id=self.product_id,
            price_cost=float(self.price_cost),
            quantity=self.quantity,
            created_at=self.created_at
        )
