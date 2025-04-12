from datetime import datetime, timezone
from typing import Optional
from uuid import uuid4

from app.domain.value_objects.document import Document
from app.domain.value_objects.email import Email
from app.domain.value_objects.name import Name


class Supplier:
    def __init__(
            self,
            supplier_id: str,
            cod: int,
            name: Name,
            document: Document,
            email: Email,
            phone: str | None,
            created_at: datetime,
    ):
        self.__supplier_id = supplier_id
        self.__cod = cod
        self.__name = name
        self.__document = document
        self.__email = email
        self.__phone = phone
        self.__created_at = created_at

    @staticmethod
    def create(
            cod: int,
            name: str,
            document: str,
            email: str,
            phone: Optional[str] = None,
    ) -> "Supplier":
        return Supplier(
            uuid4(),
            cod,
            Name(name),
            Document(document),
            Email(email),
            phone,
            datetime.now(timezone.utc),
        )

    @staticmethod
    def restore(
            supplier_id: str,
            cod: int,
            name: str,
            document: str,
            email: str,
            phone: Optional[str],
            created_at: datetime,
    ) -> "Supplier":
        return Supplier(
            supplier_id,
            cod,
            Name(name),
            Document(document),
            Email(email),
            phone,
            created_at,
        )

    def to_dict(self) -> dict:
        return {
            "supplier_id": str(self.__supplier_id),
            "cod": self.__cod,
            "name": self.__name.get_value(),
            "document": self.__document.get_value(),
            "email": self.__email.get_value(),
            "phone": self.__phone,
            "created_at": self.__created_at.isoformat(),
        }
