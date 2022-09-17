from .micro_component import MicroComponent


class Divider(MicroComponent):
    def __init__(self):
        super().__init__()

    def tick(self, time_step: int) -> None:
        super().tick(time_step)

        if len(self.prev_ints) == 2:
            self.send_func(self.prev_ints[1] // self.prev_ints[0])
