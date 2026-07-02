import requests


def find_vehicle(make, year = 2015) -> None:
    url = f"https://carapi.app/api/models/v2?make={make}&year={year}&page=1"
    response = requests.get(url)
    print(response.json())