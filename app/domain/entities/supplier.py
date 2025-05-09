from datetime import datetime, timezone
from uuid import uuid4

from app.domain.value_objects.document import Document
from app.domain.value_objects.email import Email
from app.domain.value_objects.name import Name


class Supplier:
    def __init__(
            self,
            supplier_id: str,
            cod: int | None,
            name: Name,
            document: Document | None,
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
            cod: int | None,
            name: str,
            document: str | None,
            email: str,
            phone: str | None,
    ) -> "Supplier":
        return Supplier(
            str(uuid4()),
            cod,
            Name(name),
            Document(document) if document is not None else None,
            Email(email),
            phone,
            datetime.now(timezone.utc),
        )

    @staticmethod
    def restore(
            supplier_id: str,
            cod: int | None,
            name: str,
            document: str | None,
            email: str,
            phone: str | None,
            created_at: datetime,
    ) -> "Supplier":
        return Supplier(
            supplier_id,
            cod,
            Name(name),
            Document(document) if document is not None else None,
            Email(email),
            phone,
            created_at,
        )

    def to_dict(self) -> dict:
        return {
            "supplier_id": self.__supplier_id,
            "cod": self.__cod,
            "name": self.__name.get_value(),
            "document": self.__document.get_value() if self.__document else None,
            "email": self.__email.get_value(),
            "phone": self.__phone,
            "created_at": self.__created_at.isoformat(),
        }

    def get_supplier_id(self) -> str:
        return self.__supplier_id

    def get_cod(self) -> int | None:
        return self.__cod

    def get_name(self) -> str:
        return self.__name.get_value()

    def get_document(self) -> str | None:
        return self.__document.get_value() if self.__document else None,

    def get_email(self) -> str:
        return self.__email.get_value()

    def get_phone(self) -> str | None:
        return self.__phone

    def get_created_at(self) -> str:
        return self.__created_at.isoformat()
