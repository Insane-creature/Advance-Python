# with open("weather_data.csv", mode="r") as data:
#     print(data.readlines())

import csv

with open("weather_data.csv", mode="r") as data:
    print(csv.reader(data))

