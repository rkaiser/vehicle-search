from pathlib import Path

import click

from vehicle_search.config import AppContext, ConfigError, get_config
from vehicle_search.file_read import read_vehicle_sales
from vehicle_search.rest.find import find_vehicle


@click.group()
@click.pass_context
@click.option("--config", "config_path", default=None,
              type=click.Path(exists=True, dir_okay=False, path_type=Path) )
@click.option("-f", "--force", is_flag=True)
def app(ctx: click.Context, config_path: Path, force: bool):
    """Command line tool..."""
    try:
        config = get_config(config_path)
        ctx.obj = AppContext(
            config = config,
            force = force)
    except ConfigError as exc:
        raise click.ClickException(str(exc)) from exc    

@app.command()
@click.option("-y", "--year", default=2015, help="Model year")
@click.option("-m", "--make", default="honda")
@click.pass_obj
def find(appContext: AppContext, make: str, year: int) -> None:
    """Find car by make and year"""
    click.echo(f"Finding make: {make}")
    if not appContext.force:
        #Are you sure?
        click.confirm("Are you sure you want to proceed?", abort=True)    
    find_vehicle(make, year, appContext.config.vehicle_api_url)

@app.command()
@click.option("-y", "--year", help="Sale Year",
              prompt="Enter 4 digit year of sale", type=int)
@click.option("-m", "--make", help="Make of vehicle (i.e. Honda)",
              prompt="Enter make of vehicle (i.e. Honda)")
@click.option("-o", "--model", help="Model of vehicle (i.e. Accord)",
              prompt="Enter make of vehicle (i.e. Accord)")
@click.pass_obj
def find_sales(appContext: AppContext, make: str, model: str, year: int) -> None:
    """Find car sales"""
    click.echo(f"Finding sales for make: {make}, model: {model}, year: {year}")
    if not appContext.force:
        #Are you sure?
        click.confirm("Are you sure you want to proceed?", abort=True)
    read_vehicle_sales(make, model, year, appContext.config.data_path)

@app.command("sales")
@click.argument("make", type=str)
@click.argument("model", type=str)
@click.argument("year", type=int)
@click.pass_obj
def sales(
    appContext: AppContext,
    make: str,
    model: str,
    year: int,
) -> None:
    """Find car sales"""
    click.echo(f"Finding sales for make: {make}, model: {model}, year: {year}")
    if not appContext.force:
        #Are you sure?
        click.confirm("Are you sure you want to proceed?", abort=True)
    read_vehicle_sales(make, model, year, appContext.config.data_path)

if __name__ == "__main__":
    app()