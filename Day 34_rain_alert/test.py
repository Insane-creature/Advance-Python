import requests

city_name = "Ahmedabad"
API_key = "34cc646d93c72ae9fa0987a90321e0a4"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"

response = requests.get(url)
if response == 200:
    print("Yes, we hit!")
else:
    print("Try again.")

