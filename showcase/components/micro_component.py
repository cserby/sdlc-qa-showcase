from abc import ABC, abstractmethod
from typing import Callable


class MicroComponent(ABC):
    @abstractmethod
    def initialize(self, send_func: Callable[[int], None]) -> None:
        pass

    @abstractmethod
    def receive_int(self, value: int) -> None:
        pass

    @abstractmethod
    def tick(self, time_step: int) -> None:
        pass
