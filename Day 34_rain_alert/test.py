import requests

city_name = 'New delhi'
API_key = '34cc646d93c72ae9fa0987a90321e0a4'

lat= 51.507351
long= -0.127758

url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"
OWM_Endpoint = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&appid={API_key}"


# response = requests.get(url)
response = requests.get(OWM_Endpoint)
print(response.json())

if response == 200:
    print("Yes, we hit!")
else:
    print("Try again.")

