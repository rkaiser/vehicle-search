from click.testing import CliRunner

from vehicle_search.cli import app


def test_find_command_calls_find_vehicle(monkeypatch):
    calls = []

    def mock_find_vehicle(model: str, year: int | None = None):
        calls.append((model, year))

    monkeypatch.setattr("vehicle_search.cli.find_vehicle", mock_find_vehicle)

    runner = CliRunner()
    result = runner.invoke(app, ["make", "honda"])

    assert result.exit_code == 0
    assert "Finding make: honda" in result.output
    assert calls == [("honda", None)]


def test_find_command_calls_find_vehicle_with_model_and_year(monkeypatch):
    calls = []

    def mock_find_vehicle(make: str, year: int | None = None):
        calls.append((make, year))

    monkeypatch.setattr("vehicle_search.cli.find_vehicle", mock_find_vehicle)

    runner = CliRunner()
    result = runner.invoke(app, ["find", "--make", "honda", "--year", "2020"])

    assert result.exit_code == 0
    assert "Finding make: honda" in result.output
    assert calls == [("honda", 2020)]

