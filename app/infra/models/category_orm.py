import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, String, Text, DateTime

from app.domain.entities.category import Category
from app.infra.database.base import Base


class CategoryORM(Base):
    __tablename__ = "categories"

    category_id = Column(String(36), primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    @classmethod
    def from_entity(cls, category: "Category") -> "CategoryORM":
        return cls(
            category_id=category.get_category_id(),
            name=category.get_name(),
            description=category.get_description(),
            created_at=category.get_created_at(),
        )

    def to_entity(self) -> dict:
        return Category.restore(
            category_id=self.category_id,
            name=self.name,
            description=self.description,
            created_at=self.created_at,
        ).to_dict()
