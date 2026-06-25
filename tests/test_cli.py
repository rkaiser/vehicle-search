from typer.testing import CliRunner

from vehicle_search.cli import app

runner = CliRunner()


def test_main():
    result = runner.invoke(app, ["Reid"])

    assert result.exit_code == 0
    assert result.output == "Hello Reid\n"