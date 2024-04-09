import requests
# import os
from twilio.rest import Client

account_sid = "account_sid"
auth_token = "auth_token"


API_key = "34cc646d93c72ae9fa0987a90321e0a4"
# lat= 22.092179
# long= 82.127243

lat = -33.945660
long = 151.236606

# OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}"
OWM_Endpoint = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&appid={API_key}"

# https://api.openweathermap.org/data/2.5/forecast?lat=22.092179&lon=82.127243&appid=34cc646d93c72ae9fa0987a90321e0a4

parameters = {
    "lat": 51.507351,
    "long": -0.127758,
    "appid": "34cc646d93c72ae9fa0987a90321e0a4",
    # "cnt": 4
}

response = requests.get(OWM_Endpoint, params=parameters)
# response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
weather_id = weather_data["list"]
# print(type(weather_id))
total = len(weather_id)

will_rain = False
for hour_data in range(total):
    
    condition = weather_id[hour_data]["weather"][0]["id"]
    if int(condition) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's going to rain, don't forget to carry an umbrella ☔️",
                     from_='+12564880000',
                     to='+918103500000'
                 )

    print(message.sid)