import re
from unittest.mock import MagicMock

import pytest
from showcase.components import Sender


def test_micro_controller_uninitialized_tick():
    sender = Sender()

    with pytest.raises(
        expected_exception=AssertionError,
        match=re.compile(r"not initialized", flags=re.I),
    ):
        sender.tick(5)


def test_micro_controller_uninitialized_receive_int():
    sender = Sender()

    with pytest.raises(
        expected_exception=AssertionError,
        match=re.compile(r"not initialized", flags=re.I),
    ):
        sender.receive_int(5)


def test_micro_controller_multi_init():
    sender = Sender()

    send_func_mock = MagicMock()
    sender.initialize(send_func=send_func_mock)

    send_func_mock_2 = MagicMock()

    with pytest.raises(
        expected_exception=AssertionError,
        match=re.compile(r"already initialized", flags=re.I),
    ):
        sender.initialize(send_func=send_func_mock_2)
