from .micro_component import MicroComponent


class Divider(MicroComponent):
    def __init__(self):
        super().__init__()

    def receive_int(self, value: int) -> None:
        super().receive_int(value=value)

        if self.prev_int is not None:
            # // - integer division operator
            self.send_func(value // self.prev_int)

        self.prev_int = value
