import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, String, UUID, Integer, DateTime

from app.infra.database.base import Base


class SupplierORM(Base):
    __tablename__ = "suppliers"

    supplier_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    cod = Column(Integer, unique=True, nullable=False)
    document = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    created_at = Column(
        DateTime, default=lambda: datetime.now(timezone.utc), nullable=False
    )
