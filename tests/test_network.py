import pytest
from showcase import Network


def test_network():
    network = Network()

    with pytest.raises(expected_exception=ZeroDivisionError):
        network.run(0, 5)
