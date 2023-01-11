import requests

def Get_location_latitude():
    location = requests.get(url="http://api.open-notify.org/iss-now.json")
    location.raise_for_status()

    data = location.json()
    iss_latitude = float(data["iss_position"]["latitude"])

    return iss_latitude


def Get_location_longitude():
    location = requests.get(url="http://api.open-notify.org/iss-now.json")
    location.raise_for_status()

    data = location.json()
    iss_longitude = float(data["iss_position"]["latitude"])

    return iss_longitude