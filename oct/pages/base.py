from abc import ABC, abstractmethod
from pyats.topology import Device


class Page(ABC):
    @abstractmethod
    def load(self, device: Device) -> None:
        pass

    @abstractmethod
    def available(self) -> bool:
        pass
