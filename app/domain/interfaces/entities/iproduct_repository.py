from abc import ABC, abstractmethod


class ProductRepositoryInterface(ABC):
    @abstractmethod
    def list_all(self) -> list[dict]:
        pass

    @abstractmethod
    def create(self, params: dict) -> dict:
        pass

    @abstractmethod
    def find_by_id(self, product_id: int) -> dict:
        pass
