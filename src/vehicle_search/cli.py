from pathlib import Path

import click

from vehicle_search.file_read import read_vehicle_sales
from vehicle_search.rest.find import find_vehicle


@click.group()
def app():
    """Command line tool..."""

@app.command()
@click.option("--year", default=2015, help="Model year")
@click.option("--make", default="honda")
def find(make: str, year: int) -> None:
    """Find car by make and year"""
    click.echo(f"Finding make: {make}")
    find_vehicle(make, year)

@app.command()
@click.option("--year", help="Sale Year")
@click.option("--make", help="Make of vehicle (i.e. Honda)")
@click.option("--model", help="Model of vehicle (i.e. Accord)")
@click.option("--data-path",
              help="Path to source data",
              type=click.Path(exists=True, dir_okay=False, path_type=Path))
def find_sales(make: str, model: str, year: int, data_path: Path | None) -> None:
    """Find car sales"""
    click.echo(f"Finding sales for make: {make}, model: {model}, year: {year}")
    if data_path is None:
        read_vehicle_sales(make, model, year)
    else:
        read_vehicle_sales(make, model, year, data_path)
    
if __name__ == "__main__":
    app()