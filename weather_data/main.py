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

# print(type(data)) #  #<class 'pandas.core.series.Dataframe'>
# print(type(data["temp"]))   #<class 'pandas.core.series.Series'>

df = data.to_dict()
# print(df)

# Finding the average
tl = data["temp"].to_list()
average = sum(data["temp"])/len(tl)
# print(average)

# Using pandas
print(data["temp"].mean())