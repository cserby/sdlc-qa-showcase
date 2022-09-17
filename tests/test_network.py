import pytest
from pytest import CaptureFixture
from showcase import Network


def test_network(capsys: CaptureFixture):
    network = Network()

    network.run(0, 5)

    captured = capsys.readouterr()

    assert (
        captured.out
        == """1
3
5
7
9
"""
    )
