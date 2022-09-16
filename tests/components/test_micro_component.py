import re
from unittest.mock import MagicMock

import pytest
from showcase.components import Sender


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
