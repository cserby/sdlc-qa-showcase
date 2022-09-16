from typing import Callable, Optional

from .micro_component import MicroComponent


class Sender(MicroComponent):
    def __init__(self):
        self.send_func: Optional[Callable[[int], None]] = None

    def initialize(self, send_func: Callable[[int], None]) -> None:
        assert self.send_func is None, "Already initialized"
        self.send_func = send_func

    def receive_int(self, value: int) -> None:
        pass

    def tick(self, time_step: int) -> None:
        assert self.send_func is not None, "Not initialized"
        self.send_func(time_step)
