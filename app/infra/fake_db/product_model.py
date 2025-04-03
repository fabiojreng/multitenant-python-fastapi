import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.dialects.postgresql import UUID

from app.infra.fake_db.base import Base


class ProductORM(Base):
    __tablename__ = "products"

    product_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    image = Column(String, nullable=True)
    brand_id = Column(String, nullable=False)
    category_id = Column(String, nullable=False)
    supplier_id = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    quantity_min = Column(Integer, nullable=True)
    price_cost = Column(Float, nullable=False)
    selling_price = Column(Float, nullable=False)
    validate_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    status = Column(String, nullable=False, default="ACTIVE")
