from datetime import datetime, timezone
from uuid import uuid4


class Category:
    def __init__(
            self,
            category_id: str,
            name: str,
            description: str | None,
            created_at: datetime,
    ):
        self.__category_id = category_id
        self.__name = name
        self.__description = description
        self.__created_at = created_at

    @staticmethod
    def create(name: str, description: str | None) -> "Category":
        return Category(
            str(uuid4()),
            name,
            description,
            datetime.now(timezone.utc),
        )

    @staticmethod
    def restore(
            category_id: str, name: str, description: str | None, created_at: datetime
    ) -> "Category":
        return Category(
            category_id,
            name,
            description,
            created_at,
        )

    def to_dict(self) -> dict:
        return {
            "category_id": self.__category_id,
            "name": self.__name,
            "description": self.__description,
            "created_at": self.__created_at.isoformat(),
        }

    def get_category_id(self) -> str:
        return self.__category_id

    def get_name(self) -> str:
        return self.__name

    def get_description(self) -> str | None:
        return self.__description

    def get_created_at(self) -> datetime:
        return self.__created_at
