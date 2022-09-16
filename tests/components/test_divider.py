from unittest.mock import MagicMock

from showcase.components import Divider


def test_divider_doesnt_send_when_no_ints_received():
    divider = Divider()

    send_func_mock = MagicMock()

    divider.initialize(send_func=send_func_mock)

    for i in range(10):
        divider.tick(i)

    send_func_mock.assert_not_called()


def test_divider_doesnt_send_when_one_int_received():
    divider = Divider()

    send_func_mock = MagicMock()

    divider.initialize(send_func=send_func_mock)

    divider.receive_int(5)

    for i in range(10):
        divider.tick(i)

    send_func_mock.assert_not_called()


def test_divider_sends_sum_of_last_two_ints():
    divider = Divider()

    send_func_mock = MagicMock()

    divider.initialize(send_func=send_func_mock)

    divider.receive_int(5)

    divider.receive_int(10)

    divider.receive_int(20)

    divider.tick(25)

    send_func_mock.assert_called_once_with(2)


def test_divider_sends_sum_of_last_two_ints_twice():
    divider = Divider()

    send_func_mock = MagicMock()

    divider.initialize(send_func=send_func_mock)

    for i in range(5, 8):
        divider.receive_int(i)

    divider.tick(25)

    send_func_mock.assert_called_once_with(1)

    divider.tick(26)

    send_func_mock.assert_called_with(1)

    divider.receive_int(8)

    divider.tick(27)

    send_func_mock.assert_called_with(1)
