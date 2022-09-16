from unittest.mock import MagicMock

from showcase.components import Adder


def test_adder_doesnt_send_when_no_ints_received():
    adder = Adder()

    send_func_mock = MagicMock()

    adder.initialize(send_func=send_func_mock)

    for i in range(10):
        adder.tick(i)

    send_func_mock.assert_not_called()


def test_adder_doesnt_send_when_one_int_received():
    adder = Adder()

    send_func_mock = MagicMock()

    adder.initialize(send_func=send_func_mock)

    adder.receive_int(5)

    for i in range(10):
        adder.tick(i)

    send_func_mock.assert_not_called()


def test_adder_sends_sum_of_last_two_ints():
    adder = Adder()

    send_func_mock = MagicMock()

    adder.initialize(send_func=send_func_mock)

    adder.receive_int(5)

    adder.receive_int(6)

    adder.receive_int(7)

    adder.tick(25)

    send_func_mock.assert_called_once_with(13)


def test_adder_sends_sum_of_last_two_ints_twice():
    adder = Adder()

    send_func_mock = MagicMock()

    adder.initialize(send_func=send_func_mock)

    for i in range(5, 8):
        adder.receive_int(i)

    adder.tick(25)

    send_func_mock.assert_called_once_with(13)

    adder.tick(26)

    send_func_mock.assert_called_with(13)

    adder.receive_int(8)

    adder.tick(27)

    send_func_mock.assert_called_with(15)
