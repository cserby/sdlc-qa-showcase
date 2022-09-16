from .micro_component import MicroComponent


class Adder(MicroComponent):
    def __init__(self):
        super().__init__()

    def receive_int(self, value: int) -> None:
        super().receive_int(value=value)

        if self.prev_int is not None:
            self.send_func(self.prev_int + value)

        self.prev_int = value
