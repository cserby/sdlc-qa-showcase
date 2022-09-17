from pytest import CaptureFixture
from showcase.components import Writer


def test_writer_multi(capsys: CaptureFixture[str]):
    writer = Writer()

    writer.tick(1)

    assert capsys.readouterr().out == ""

    writer.receive_int(4)

    assert capsys.readouterr().out == ""

    writer.tick(1)

    assert capsys.readouterr().out == "4\n"

    writer.tick(2)

    assert capsys.readouterr().out == ""

    writer.receive_int(12314)

    writer.tick(3)

    assert capsys.readouterr().out == "12314\n"
