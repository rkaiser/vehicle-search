from click.testing import CliRunner

from vehicle_search.cli import app


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

def test_find_command_calls_find_sales_with_make_model_and_year(monkeypatch):
    calls = []

    def mock_read_vehicle_sales(make: str, model: str, year: int):
        calls.append((make, model, year))

    monkeypatch.setattr("vehicle_search.cli.read_vehicle_sales", mock_read_vehicle_sales)

    runner = CliRunner()
    result = runner.invoke(app, ["find-sales", "--make", "honda", "--model", "accord",
                                "--year", 2020])

    assert result.exit_code == 0
    assert "Finding sales for make: honda, model: accord, year: 2020" in result.output
    assert calls == [("honda", "accord", "2020")]

def test_find_command_calls_find_sales_with_make_model_year_and_data(monkeypatch, tmp_path):
    calls = []

    data_file = tmp_path / "data.csv"
    data_file.write_text("year,make,model\n2020,honda,accord\n")

    def mock_read_vehicle_sales(make: str, model: str, year: int, data_path: str | None):
        calls.append((make, model, year, data_path))

    monkeypatch.setattr("vehicle_search.cli.read_vehicle_sales", mock_read_vehicle_sales)

    runner = CliRunner()
    result = runner.invoke(app, ["find-sales", "--make", "honda", "--model", "accord",
                                "--year", 2020, "--data-path", str(data_file)])

    assert result.exit_code == 0
    assert "Finding sales for make: honda, model: accord, year: 2020" in result.output
    assert calls == [("honda", "accord", "2020", data_file)]