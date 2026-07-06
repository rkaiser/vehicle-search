from pathlib import Path

import click

from vehicle_search.config import ConfigError, get_config
from vehicle_search.file_read import read_vehicle_sales
from vehicle_search.rest.find import find_vehicle


@click.group()
def app():
    """Command line tool..."""

@app.command()
@click.option("--config", "config_path", default=None,
              type=click.Path(exists=True, dir_okay=False, path_type=Path) )
@click.option("--year", default=2015, help="Model year")
@click.option("--make", default="honda")
def find(make: str, year: int, config_path: Path) -> None:
    """Find car by make and year"""
    config = get_config(config_path)
    click.echo(f"Finding make: {make}")
    find_vehicle(make, year, config.vehicle_api_url)

@app.command()
@click.option("--config", "config_path", default=None,
              type=click.Path(exists=True, dir_okay=False, path_type=Path) )
@click.option("--year", help="Sale Year")
@click.option("--make", help="Make of vehicle (i.e. Honda)")
@click.option("--model", help="Model of vehicle (i.e. Accord)")
@click.option("--data-path",
              help="Path to source data",
              type=click.Path(exists=True, dir_okay=False, path_type=Path))
def find_sales(make: str, model: str, year: int, config_path: Path | None,
               data_path: Path | None) -> None:
    """Find car sales"""
    try:
        config = get_config(config_path)
    except ConfigError as exc:
        raise click.ClickException(str(exc)) from exc
    
    click.echo(f"Finding sales for make: {make}, model: {model}, year: {year}")
    if data_path is not None:
        config = config.__class__(
            data_path=data_path,
            vehicle_api_url=config.vehicle_api_url
        )
    click.echo(f"Finding sales for make: {make}, model: {model}, year: {year} " \
               f"using path {config.data_path}")
    read_vehicle_sales(make, model, year, config.data_path)
if __name__ == "__main__":
    app()