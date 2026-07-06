from pathlib import Path

from click.testing import CliRunner

from vehicle_search.cli import app
from vehicle_search.config import AppConfig


def test_find_command_calls_find_vehicle_with_model_and_year(monkeypatch, tmp_path):
    calls = []

    known_config = AppConfig(
        data_path="/tmp/test-sales.csv",
        vehicle_api_url="https://test.url"
    )
    data_file = tmp_path / "data.csv"
    data_file.write_text("year,make,model\n2020,honda,accord\n")

    def mock_find_vehicle(make: str, year: int | None, url: str):
        calls.append((make, year, url))
    def mock_get_config(config_path: Path):
        calls.append(config_path)
        return known_config

    monkeypatch.setattr("vehicle_search.cli.find_vehicle", mock_find_vehicle)
    monkeypatch.setattr("vehicle_search.cli.get_config", mock_get_config)

    runner = CliRunner()
    result = runner.invoke(app, ["find", "--make", "honda", "--year", "2020",
                                  "--config", str(data_file)])

    assert result.exit_code == 0
    assert "Finding make: honda" in result.output
    assert calls[1] == ("honda", 2020, known_config.vehicle_api_url)

def test_find_command_calls_find_sales_with_make_model_and_year(monkeypatch, tmp_path):
    calls = []
    known_config = AppConfig(
        data_path="/tmp/test-sales.csv",
        vehicle_api_url="https://test.url"
    )
    data_file = tmp_path / "data.csv"
    data_file.write_text("year,make,model\n2020,honda,accord\n")

    def mock_read_vehicle_sales(make: str, model: str, year: int, config_path: Path):
        calls.append((make, model, year, config_path))
    def mock_get_config(config_path: Path):
        calls.append(config_path)
        return known_config

    monkeypatch.setattr("vehicle_search.cli.read_vehicle_sales", mock_read_vehicle_sales)
    monkeypatch.setattr("vehicle_search.cli.get_config", mock_get_config)

    runner = CliRunner()
    result = runner.invoke(app, ["find-sales", "--make", "honda", "--model", "accord",
                                "--year", "2020", "--config", str(data_file)])

    assert result.exit_code == 0
    assert "Finding sales for make: honda, model: accord, year: 2020" in result.output
    assert calls[1] == ("honda", "accord", "2020", known_config.data_path)

def test_find_command_calls_find_sales_with_make_model_year_and_data(monkeypatch, tmp_path):
    calls = []

    known_config = AppConfig(
        data_path="/tmp/test-sales.csv",
        vehicle_api_url="https://test.url"
    )
    data_file = tmp_path / "data.csv"
    data_file.write_text("year,make,model\n2020,honda,accord\n")

    def mock_read_vehicle_sales(make: str, model: str, year: int, data_path: str | None):
        calls.append((make, model, year, data_path))
    def mock_get_config(config_path: Path):
        calls.append(config_path)
        return known_config
    
    monkeypatch.setattr("vehicle_search.cli.read_vehicle_sales", mock_read_vehicle_sales)
    monkeypatch.setattr("vehicle_search.cli.get_config", mock_get_config)

    runner = CliRunner()
    result = runner.invoke(app, ["find-sales", "--make", "honda", "--model", "accord",
                                "--year", "2020", "--config", str(data_file)])

    assert result.exit_code == 0
    assert "Finding sales for make: honda, model: accord, year: 2020" in result.output
    assert calls[1] == ("honda", "accord", "2020", known_config.data_path)