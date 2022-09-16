from typing import List

from .components import Adder, Divider, MicroComponent, Sender, Writer


class Network:
    def __init__(self):
        self.sender: Sender = Sender()
        self.adder: Adder = Adder()
        self.divider: Divider = Divider()
        self.writer: Writer = Writer()
        self.components: List[MicroComponent] = [
            self.sender,
            self.adder,
            self.divider,
            self.writer,
        ]

        def sender_send_func(value: int) -> None:
            self.adder.receive_int(value)
            self.divider.receive_int(value)

        self.sender.initialize(send_func=sender_send_func)

        def adder_send_func(value: int) -> None:
            self.divider.receive_int(value)
            self.writer.receive_int(value)

        self.adder.initialize(send_func=adder_send_func)

        def divider_send_func(value: int) -> None:
            self.writer.receive_int(value)

        self.divider.initialize(send_func=divider_send_func)

    def run(self, start_tick: int, end_tick: int) -> None:
        for tick in range(start_tick, end_tick + 1):
            for component in self.components:
                component.tick(time_step=tick)
