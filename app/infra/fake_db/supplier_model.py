from sqlalchemy import Column, String, UUID, Integer, DateTime
from sqlalchemy.orm import declarative_base
from app.infra.fake_db.base import Base
from datetime import datetime, date, timezone
import uuid


class SupplierORM(Base):
    __tablename__ = "suppliers"

    supplier_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    cod = Column(Integer, unique=True, nullable=False)
    name = Column(String, nullable=False)
    document = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    created_at = Column(
        DateTime, default=lambda: datetime.now(timezone.utc), nullable=False
    )
