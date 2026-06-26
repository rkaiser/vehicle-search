import click

from vehicle_search.rest.find import find_vehicle


@click.group()
def app():
    """Command line tool..."""

@app.command()
@click.argument("make")
def make(make: str) -> None:
    """Find car by make"""
    click.echo(f"Finding make: {make}")
    find_vehicle(make)


@app.command()
@click.option("--year", default=2015, help="Model year")
@click.option("--make", default="honda")
def find(make: str, year: int) -> None:
    """Find car by make and year"""
    click.echo(f"Finding make: {make}")
    find_vehicle(make, year)

if __name__ == "__main__":
    app()