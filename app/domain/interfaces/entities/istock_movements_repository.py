from abc import ABC, abstractmethod


class StockMovementsRepositoryInterface(ABC):
    @abstractmethod
    def list_all(self) -> list[dict]:
        pass

    @abstractmethod
    def create(self, params: dict) -> dict:
        pass
