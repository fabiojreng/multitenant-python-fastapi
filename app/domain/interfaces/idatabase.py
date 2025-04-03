from abc import ABC, abstractmethod

class ConnectionDBInterface(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @abstractmethod
    def get_session(self):
        pass
