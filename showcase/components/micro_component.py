from abc import ABC
from typing import Callable, Optional


class MicroComponent(ABC):
    def __init__(self):
        self.initialized: bool = False
        self.send_func: Callable[[int], None] = lambda _: None
        self.prev_int: Optional[int] = None

    def initialize(self, send_func: Callable[[int], None]) -> None:
        assert not self.initialized, "Already initialized"
        self.send_func = send_func
        self.initialized = True

    def receive_int(self, value: int) -> None:
        pass

    def tick(self, time_step: int) -> None:
        pass
