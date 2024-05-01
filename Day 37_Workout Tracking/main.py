import requests

APP_ID = "54d93fe7"
API_KEY = "1c81a7c1eb06694263a3c035c45b1896"

GENDER = "Female"
WEIGHT_KG = 58
HEIGHT_CM = 168
AGE = 22

host_domain = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(host_domain, json=parameters, headers=headers)
print(response.text)
