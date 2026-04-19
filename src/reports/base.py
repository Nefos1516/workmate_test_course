from abc import ABC, abstractmethod


class BaseReport(ABC):
    @abstractmethod
    def generate(self, data: list[dict]) -> list[dict]:
        pass