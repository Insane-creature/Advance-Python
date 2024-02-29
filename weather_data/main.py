# with open("weather_data.csv", mode="r") as data:
#     print(data.readlines())

# import csv

# with open("weather_data.csv", mode="r") as data:
#     data_file = csv.reader(data)
#     temperatures = []
#     data.read
#     for row in data_file:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
#     print(type(temperatures))

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])