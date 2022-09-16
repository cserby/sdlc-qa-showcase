from .micro_component import MicroComponent


class Writer(MicroComponent):
    def __init__(self):
        super().__init__()

    def receive_int(self, value: int) -> None:
        super().receive_int(value=value)

        print(value)
