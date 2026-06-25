import requests


def findVehicle(make):
    url = f"https://carapi.app/api/models/v2?make={make}&year=2017&page=1"
    response = requests.get(url)
    print(response.json())