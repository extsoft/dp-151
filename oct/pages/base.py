from abc import ABC, abstractmethod


class Page(ABC):
    @abstractmethod
    def open(self) -> None:
        pass

    @abstractmethod
    def loaded(self) -> bool:
        pass
