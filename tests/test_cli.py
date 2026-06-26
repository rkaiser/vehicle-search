from click.testing import CliRunner

from vehicle_search.cli import app

runner = CliRunner()


def test_main():
    result = runner.invoke(app, ["make", "honda"])

    assert result.exit_code == 0
    assert "Finding make: honda" in result.output

def test_find_command_with_defaults():
    runner = CliRunner()

    result = runner.invoke(app, ["find"])

    assert result.exit_code == 0
    assert "Finding make: honda" in result.output

def test_find_command_with_options():
    runner = CliRunner()

    result = runner.invoke(app, ["find", "--make", "honda", "--year", "2017"])

    assert result.exit_code == 0
    assert "Finding make: honda" in result.output
