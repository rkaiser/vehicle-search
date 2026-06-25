import typer

from vehicle_search.rest.find import findVehicle

app = typer.Typer()


@app.command()
def goodby(name: str):
    print(f"Goodbye {name}")

@app.command()
def hello(name: str):
    print(f"Hello {name}")

@app.command()
def find(name: str):
    print(f"finding {name}")
    findVehicle(name)


if __name__ == "__main__":
    app()
