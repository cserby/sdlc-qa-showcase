from .micro_component import MicroComponent


class Sender(MicroComponent):
    def __init__(self):
        super().__init__()

    def tick(self, time_step: int) -> None:
        super().tick(time_step=time_step)
        self.send_func(time_step)
