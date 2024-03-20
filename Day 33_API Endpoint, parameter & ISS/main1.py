import requests
from datetime import datetime

my_lat = 23.022505
my_long = 72.571365

today_date = datetime.now()
print("----------")
print(today_date)

parameters = {
    "lat": my_lat,
    "long": my_long,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

today_date = datetime.time
print("----------")
print(today_date)

