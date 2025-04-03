from abc import ABC, abstractmethod
from typing import Any


class UseCaseInterface(ABC):
    @abstractmethod
    def execute(self, params: Any = None) -> dict:
        pass
