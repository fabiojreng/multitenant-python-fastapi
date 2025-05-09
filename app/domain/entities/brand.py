from datetime import datetime, timezone
from uuid import uuid4


class Brand:
    def __init__(
            self,
            brand_id: str,
            name: str,
            description: str | None,
            created_at: datetime,
    ):
        self.__brand_id = brand_id
        self.__name = name
        self.__description = description
        self.__created_at = created_at

    @staticmethod
    def create(name: str, description: str | None) -> "Brand":
        return Brand(
            str(uuid4()),
            name,
            description,
            datetime.now(timezone.utc),
        )

    @staticmethod
    def restore(
            brand_id: str, name: str, description: str | None, created_at: datetime
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

    def get_brand_id(self) -> str:
        return self.__brand_id

    def get_name(self) -> str:
        return self.__name

    def get_description(self) -> str:
        return self.__description

    def get_created_at(self) -> str:
        return str(self.__created_at)
