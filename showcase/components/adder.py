from .micro_component import MicroComponent


class Adder(MicroComponent):
    def __init__(self):
        super().__init__()

    def tick(self, time_step: int) -> None:
        super().tick(time_step=time_step)
        assert self.send_func is not None

        if len(self.prev_ints) == 2:
            self.send_func(sum(self.prev_ints))
