import requests

API_key = "34cc646d93c72ae9fa0987a90321e0a4"
lat= 22.092179
long= 82.127243

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
print(weather_data["list"][0]["weather"][0]["id"])
# print(weather_data["list"][0]["weather"]["id"])

# will_rain = False
# for hour_data in weather_data["list"]:
#     condition_data = hour_data["weather"][0]["id"]
#     if int(condition_data) < 700:
#         will_rain = True

# if will_rain:
#     print("Bring an umbrella.")