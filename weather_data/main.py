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

# print(data)
# print(data["temp"])
# print(type(data)) #  #<class 'pandas.core.series.Dataframe'>
# print(type(data["temp"]))   #<class 'pandas.core.series.Series'>

df = data.to_dict()
# print(df)

tl = data["temp"].to_list()
average = sum(data["temp"])/len(tl)

# print(average)
# print(data["temp"].mean())
# print(data["temp"].max())

# print(data["condition"])  # print(data.temp)

# print(data.temp[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

day_temp = data.temp[0]
day_temp = data.temp[data.day == "Monday"]
# converting_to_fahrenheit = (day_temp * 1.8) + 32
# print(converting_to_fahrenheit)

# Creating a dataframe from Scratch
data_dict = {
    "student": ["Amy","Ashu","Anshika"],
    "scores": [76, 34, 89],
}

# data1 = pandas.DataFrame(data_dict)
# print(data1)
# print(type(data1))      # pandas.core.frame.DataFrame
# print(type(data_dict))  # dict

# data1.to_csv("student_data.csv")

squireel_data = pandas.read_csv("Squirrel_Census.csv")
gray_squireels = squireel_data[squireel_data["Primary Fur Color"] == "Gray"]
gray_squireels_count = len(squireel_data[squireel_data["Primary Fur Color"] == "Gray"])

Cinnamon_squireels = squireel_data[squireel_data["Primary Fur Color"] == "Cinnamon"]
Cinnamon_squireels_count = len(squireel_data[squireel_data["Primary Fur Color"] == "Cinnamon"])

Black_squireels = squireel_data[squireel_data["Primary Fur Color"] == "Black"]
Black_squireels_count = len(squireel_data[squireel_data["Primary Fur Color"] == "Black"])

print(list(set(squireel_data["Primary Fur Color"])))

# print(gray_squireels_count)
# print(Cinnamon_squireels_count)
# print(Black_squireels_count)

# print(squireel_data["Primary Fur Color"])
# print(squireel_data)

data_dict = {
    "Fun Color": ["Gray", "Black","Cinnamon"],
    "Count": [gray_squireels_count, Black_squireels_count, Cinnamon_squireels_count]
}

# pandas.DataFrame(data_dict).to_csv("Squirrel_count.csv")