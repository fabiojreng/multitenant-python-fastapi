from abc import ABC, abstractmethod


class ProductRepositoryInterface(ABC):
    @abstractmethod
    def list_all(self) -> list[dict]:
        pass

    @abstractmethod
    def create(self, params: dict) -> dict:
        pass
