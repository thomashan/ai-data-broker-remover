from abc import ABC, abstractmethod

class DataSource(ABC):
    @abstractmethod
    def get_brokers(self, url: str) -> list[str]:
        pass
