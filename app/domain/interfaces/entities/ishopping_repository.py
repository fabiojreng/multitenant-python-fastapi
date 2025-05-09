from abc import ABC, abstractmethod

from app.domain.entities.shopping import Shopping


class ShoppingRepositoryInterface(ABC):
    @abstractmethod
    def create(self, shopping: Shopping) -> None:
        pass
