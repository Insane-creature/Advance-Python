import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_keys = "34cc646d93c72ae9fa0987a90321e0a4"

parameters = {
    "lat": 23.022505,
    "long": 72.571365,
    "appid": api_keys,
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_data = hour_data["weather"][0]["id"]
    if int(condition_data) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")