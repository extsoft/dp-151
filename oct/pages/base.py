from abc import ABC, abstractmethod
from pyats.topology import Device


class Page(ABC):
    @abstractmethod
    def open(self, device: Device) -> None:
        pass

    @abstractmethod
    def loaded(self) -> bool:
        pass
