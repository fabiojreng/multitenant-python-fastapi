from datetime import datetime, timezone

from sqlalchemy import Column, String, Text, DateTime

from app.domain.entities.brand import Brand
from app.infra.database.base import Base


class BrandORM(Base):
    __tablename__ = "brands"

    brand_id = Column(String(36), primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

    @classmethod
    def from_entity(cls, brand: "Brand") -> "BrandORM":
        return cls(
            brand_id=brand.get_brand_id(),
            name=brand.get_name(),
            description=brand.get_description(),
            created_at=brand.get_created_at(),
        )

    def to_entity(self) -> "Brand":
        return Brand.restore(
            brand_id=self.brand_id,
            name=self.name,
            description=self.description,
            created_at=self.created_at
        ).to_dict()
