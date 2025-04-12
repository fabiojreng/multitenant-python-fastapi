from abc import ABC, abstractmethod

from app.presentation.schemas.response_schema import SchemaResponseHttp


class UseCaseInterface(ABC):
    @abstractmethod
    def execute(self, params: dict = None) -> SchemaResponseHttp:
        pass
