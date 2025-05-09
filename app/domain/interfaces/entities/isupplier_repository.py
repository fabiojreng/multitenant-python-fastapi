from abc import ABC, abstractmethod


class SupplierRepositoryInterface(ABC):
    @abstractmethod
    def list_all(self) -> list[dict]:
        pass

    @abstractmethod
    def create(self, params: dict) -> list[dict]:
        pass

    @abstractmethod
    def find_by_id(self, supplier_id: str) -> dict:
        pass

    @abstractmethod
    def find_by_email(self, supplier_id: str) -> dict:
        pass
