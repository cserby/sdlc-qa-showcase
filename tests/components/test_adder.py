from unittest.mock import MagicMock

from showcase.components import Adder


def test_adder_doesnt_send_when_first_int_received():
    adder = Adder()

    send_func_mock = MagicMock()

    adder.initialize(send_func=send_func_mock)

    adder.receive_int(1)

    send_func_mock.assert_not_called()


def test_adder_sends_sum_when_two_ints_received():
    adder = Adder()

    send_func_mock = MagicMock()

    adder.initialize(send_func=send_func_mock)

    adder.receive_int(1)

    adder.receive_int(2)

    send_func_mock.assert_called_once_with(3)


def test_adder_sends_sum_of_last_two_when_many_ints_received():
    adder = Adder()

    send_func_mock = MagicMock()

    adder.initialize(send_func=send_func_mock)

    for i in range(3, 20, 3):
        adder.receive_int(i)

    send_func_mock.assert_called_with(18 + 15)


def test_adder_tick_does_nothing():
    adder = Adder()

    send_func_mock = MagicMock()

    adder.initialize(send_func=send_func_mock)

    for i in range(3):
        adder.tick(i)

    send_func_mock.assert_not_called()
