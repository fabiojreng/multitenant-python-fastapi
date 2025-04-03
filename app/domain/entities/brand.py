from uuid import uuid4
from datetime import datetime, timezone
from typing import Optional


class Brand:
    def __init__(
        self,
        brand_id: str,
        name: str,
        description: Optional[str],
        created_at: datetime,
    ):
        self.__brand_id = brand_id
        self.__name = name
        self.__description = description
        self.__created_at = created_at

    @staticmethod
    def create(name: str, description: Optional[str] = None) -> "Brand":
        return Brand(
            uuid4(),
            name,
            description,
            datetime.now(timezone.utc),
        )

    @staticmethod
    def restore(
        brand_id: str, name: str, description: Optional[str], created_at: datetime
    ) -> "Brand":
        return Brand(
            brand_id,
            name,
            description,
            created_at,
        )

    def to_dict(self) -> dict:
        return {
            "brand_id": self.__brand_id,
            "name": self.__name,
            "description": self.__description,
            "created_at": self.__created_at.isoformat(),
        }
