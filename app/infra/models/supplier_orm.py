import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, String, Integer, DateTime

from app.domain.entities.supplier import Supplier
from app.infra.database.base import Base


class SupplierORM(Base):
    __tablename__ = "suppliers"

    supplier_id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    cod = Column(Integer, unique=True, nullable=True)
    document = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    @classmethod
    def from_entity(cls, supplier: Supplier) -> "SupplierORM":
        return cls(
            supplier_id=supplier.get_supplier_id(),
            cod=supplier.get_cod(),
            name=supplier.get_name(),
            document=supplier.get_document(),
            email=supplier.get_email(),
            phone=supplier.get_phone(),
            created_at=supplier.get_created_at(),
        )

    def to_entity(self) -> Supplier:
        return Supplier.restore(
            supplier_id=self.supplier_id,
            cod=self.cod,
            name=self.name,
            document=self.document,
            email=self.email,
            phone=self.phone,
            created_at=self.created_at
        ).to_dict()
