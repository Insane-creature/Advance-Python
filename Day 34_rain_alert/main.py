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
# response.raise_for_status()
print(response.status_code)
weather_data = response.json()
print(weather_data)
# # question_data = data["results"]
# print(data)