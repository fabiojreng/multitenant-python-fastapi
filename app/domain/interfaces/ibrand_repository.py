from abc import ABC, abstractmethod


class BrandRepositoryInterface(ABC):
    @abstractmethod
    def save(self, brand: dict) -> None:
        pass

    def fetch_all(self) -> list[dict]:
        pass

    def find_by_id(self, id: str) -> dict:
        pass
