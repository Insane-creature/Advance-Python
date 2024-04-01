import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast?q=London,us&mode=xml&appid={API key}"
api_keys = "34cc646d93c72ae9fa0987a90321e0a4"

parameters = {
    "lat": 51.507351,
    "long": -0.127758,
    "appid": "635ba07154facb3e484a55a532b44c33"
    # "cnt": 4
}

response = requests.get(OWM_Endpoint, params=parameters)
# response.raise_for_status()
print(response.json())
# print(weather_data["list"][0]["weather"]["id"])

# will_rain = False
# for hour_data in weather_data["list"]:
#     condition_data = hour_data["weather"][0]["id"]
#     if int(condition_data) < 700:
#         will_rain = True

# if will_rain:
#     print("Bring an umbrella.")