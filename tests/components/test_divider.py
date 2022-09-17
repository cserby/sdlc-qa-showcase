from unittest.mock import MagicMock, call

import pytest
from showcase.components import Divider


def test_divider_doesnt_send_when_first_int_received():
    divider = Divider()

    send_func_mock = MagicMock()

    divider.initialize(send_func=send_func_mock)

    divider.receive_int(1)

    divider.tick(1)

    send_func_mock.assert_not_called()


def test_divider_sends_ratio_when_two_ints_received():
    divider = Divider()

    send_func_mock = MagicMock()

    divider.initialize(send_func=send_func_mock)

    divider.receive_int(6)

    divider.receive_int(48)

    send_func_mock.assert_not_called()

    divider.tick(1)

    send_func_mock.assert_called_once_with(8)


def test_divider_sends_ratio_of_last_two_when_many_ints_received():
    divider = Divider()

    send_func_mock = MagicMock()

    divider.initialize(send_func=send_func_mock)

    for i in range(300, 2000, 72):
        divider.receive_int(i)

    divider.tick(1)

    send_func_mock.assert_called_with(1)


def test_divider_two_ticks_send_the_same():
    divider = Divider()

    send_func_mock = MagicMock()

    divider.initialize(send_func=send_func_mock)

    for i in range(300, 2000, 72):
        divider.receive_int(i)

    divider.tick(1)
    divider.tick(2)

    send_func_mock.assert_has_calls([call(1), call(1)])


def test_divider_division_by_zero():
    divider = Divider()

    send_func_mock = MagicMock()

    divider.initialize(send_func=send_func_mock)

    for i in range(2):
        divider.receive_int(i)

    send_func_mock.assert_not_called()

    with pytest.raises(expected_exception=ZeroDivisionError):
        divider.tick(1)

    send_func_mock.assert_not_called()
