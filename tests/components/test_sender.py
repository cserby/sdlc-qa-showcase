from unittest.mock import MagicMock

from showcase.components import Sender


def test_sender_tick():
    sender = Sender()

    send_func_mock = MagicMock()

    sender.initialize(send_func=send_func_mock)
    sender.tick(5)

    send_func_mock.assert_called_once_with(5)


def test_sender_receive_int():
    sender = Sender()

    send_func_mock = MagicMock()

    sender.initialize(send_func=send_func_mock)
    sender.receive_int(5)

    send_func_mock.assert_not_called()
