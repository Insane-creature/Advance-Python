import requests
from datetime import datetime as dt
import smtplib
import time

MY_EMAIL = "anshikasoni323@gmail.com"
MY_PASSWORD = "abcde@123"

my_lat = 22.089065
my_long = 82.127773

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    # print(response.status_code) -- traditional way
    data = response.json()
    # print(data)

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    # my position within iss
    if my_lat - 5 <= iss_latitude <= my_lat + 5 and my_long - 5 <= iss_longitude <= my_lat + 5:
        return True

def is_night():
    parameters = {
        "lat": my_lat,
        "long": my_long,
        "formatted": 0
    }

    # iss_position = (longitude, latitude)
    # print(iss_position)

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Hurry! Look up\n\n See above the sky, the ISS is above."
        )