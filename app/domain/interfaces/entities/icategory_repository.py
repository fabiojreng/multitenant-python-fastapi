from abc import ABC, abstractmethod


class CategoryRepositoryInterface(ABC):
    @abstractmethod
    def list_all(self) -> list[dict]:
        pass

    @abstractmethod
    def create(self, params: dict) -> list[dict]:
        pass

    @abstractmethod
    def find_by_id(self, category_id: str) -> dict:
        pass
