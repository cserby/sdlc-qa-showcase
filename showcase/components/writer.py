from .micro_component import MicroComponent


class Writer(MicroComponent):
    def __init__(self):
        super().__init__()

    def tick(self, time_step: int) -> None:
        super().tick(time_step)
        if len(self.prev_ints) > 0:
            print(self.prev_ints[0])
        self.prev_ints = []
