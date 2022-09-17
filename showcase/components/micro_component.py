import logging
from abc import ABC
from typing import Callable, List


class MicroComponent(ABC):
    def __init__(self):
        self.initialized: bool = False
        self.send_func: Callable[[int], None] = lambda _: None
        self.prev_ints: List[int] = []
        self.logger: logging.Logger = logging.getLogger(str(self))

    def initialize(self, send_func: Callable[[int], None]) -> None:
        self.logger.debug("initialize(...)")
        assert not self.initialized, "Already initialized"
        self.send_func = send_func
        self.initialized = True

    def receive_int(self, value: int) -> None:
        self.logger.debug(f"receive_int({value})")
        self.prev_ints = (self.prev_ints + [value])[-2:]

    def tick(self, time_step: int) -> None:
        self.logger.debug(f"tick({time_step}) with {self.prev_ints}")
