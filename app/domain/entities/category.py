from uuid import uuid4
from datetime import datetime, timezone
from typing import Optional


class Category:
    def __init__(
        self,
        category_id: str,
        name: str,
        description: Optional[str],
        created_at: datetime,
    ):
        self.__category_id = category_id
        self.__name = name
        self.__description = description
        self.__created_at = created_at

    @staticmethod
    def create(name: str, description: Optional[str] = None) -> "Category":
        return Category(
            uuid4(),
            name,
            description,
            datetime.now(timezone.utc),
        )

    @staticmethod
    def restore(
        category_id: str, name: str, description: Optional[str], created_at: datetime
    ) -> "Category":
        return Category(
            category_id,
            name,
            description,
            created_at,
        )
