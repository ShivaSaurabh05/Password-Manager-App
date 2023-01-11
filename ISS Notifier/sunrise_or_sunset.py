import requests
from datetime import datetime

My_lat = 25.460854
My_lng = 85.559508

parameters = {
    "lat": My_lat,
    "lng": My_lng,
    "formatted": 0,

}

def sunrise_time():
    rise_or_set = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    rise_or_set.raise_for_status()

    data = rise_or_set.json()

    sunrise = data["results"]["sunrise"]
    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])

    return sunrise_hour

def sunset_time():
    rise_or_set = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    rise_or_set.raise_for_status()

    data = rise_or_set.json()

    sunset = data["results"]["sunset"]
    sunset_hour = int(sunset.split("T")[1].split(":")[0])


    return sunset_hour




