from pytest import CaptureFixture
from showcase.components import Writer


def test_writer_multi(capsys: CaptureFixture[str]):
    writer = Writer()

    writer.receive_int(4)

    writer.receive_int(12314)

    captured = capsys.readouterr()

    assert captured.out == "4\n12314\n"
