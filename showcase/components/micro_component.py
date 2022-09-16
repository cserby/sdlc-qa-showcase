from abc import ABC, abstractmethod
from typing import Callable, List, Optional


class MicroComponent(ABC):
    def __init__(self):
        self.send_func: Optional[Callable[[int], None]] = None
        self.prev_ints: List[int] = []

    def initialize(self, send_func: Callable[[int], None]) -> None:
        assert self.send_func is None, "Already initialized"
        self.send_func = send_func

    def receive_int(self, value: int) -> None:
        self.prev_ints = (self.prev_ints + [value])[-2:]

    @abstractmethod
    def tick(self, time_step: int) -> None:
        assert self.send_func is not None, "Not initialized"
