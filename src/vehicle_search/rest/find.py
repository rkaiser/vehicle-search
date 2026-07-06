import requests


def find_vehicle(make, year, url) -> None:
    url = f"{url}?make={make}&year={year}&page=1"
    response = requests.get(url)
    print(response.json())