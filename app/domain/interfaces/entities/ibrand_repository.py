from abc import ABC, abstractmethod


class BrandRepositoryInterface(ABC):
    @abstractmethod
    def list_all(self) -> list[dict]:
        pass

    @abstractmethod
    def create(self, params: dict) -> list[dict]:
        pass

    @abstractmethod
    def find_by_id(self, brand_id: str) -> dict:
        pass
