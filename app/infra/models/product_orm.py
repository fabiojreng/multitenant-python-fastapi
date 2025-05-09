from datetime import datetime, timezone

from sqlalchemy import Column, String, Text, ForeignKey, Integer, Numeric, Date, DateTime, Enum as SAEnum
from sqlalchemy.orm import relationship

from app.domain.entities.product import Product
from app.domain.value_objects.status import ProductStatus
from app.infra.database.base import Base


class ProductORM(Base):
    __tablename__ = "products"

    product_id = Column(String(36), primary_key=True)
    name = Column(String(255), nullable=False)
    image = Column(Text, nullable=True)

    brand_id = Column(String(36), ForeignKey("brands.brand_id"), nullable=True)
    category_id = Column(String(36), ForeignKey("categories.category_id"), nullable=True)
    supplier_id = Column(String(36), ForeignKey("suppliers.supplier_id"), nullable=False)

    quantity = Column(Integer, nullable=False)
    quantity_min = Column(Integer, nullable=True)

    price_cost = Column(Numeric(10, 2), nullable=False)
    selling_price = Column(Numeric(10, 2), nullable=False)

    validate_date = Column(Date, nullable=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    status = Column(SAEnum(ProductStatus, values_callable=lambda enum: [e.value for e in enum]), nullable=False,
                    default=ProductStatus.ACTIVE)

    shoppings = relationship("ShoppingORM", back_populates="product")

    @classmethod
    def from_entity(cls, product: "Product") -> "ProductORM":
        return cls(
            product_id=product.get_product_id(),
            name=product.get_name(),
            image=product.get_image(),
            brand_id=product.get_brand_id(),
            category_id=product.get_category_id(),
            supplier_id=product.get_supplier_id(),
            quantity=product.get_quantity(),
            quantity_min=product.get_quantity_min(),
            price_cost=product.get_price_cost(),
            selling_price=product.get_selling_price(),
            validate_date=product.get_validate_date(),
            created_at=product.get_created_at(),
            status=product.get_status()
        )

    def to_entity(self) -> "Product":
        return Product.restore(
            product_id=self.product_id,
            name=self.name,
            quantity=self.quantity,
            price_cost=float(self.price_cost),
            selling_price=float(self.selling_price),
            created_at=str(self.created_at),
            status=self.status.value,
            brand_id=str(self.brand_id) if self.brand_id else None,
            category_id=str(self.category_id) if self.category_id else None,
            supplier_id=str(self.supplier_id),
            image=self.image,
            quantity_min=self.quantity_min,
            validate_date=self.validate_date,
        ).to_dict()
