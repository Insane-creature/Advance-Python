import smtplib
import datetime as dt
import random
import pandas as pd

my_email = "anshika@gmail.com"
password = "znexlybeihcnsruv"

now = dt.datetime.now()
# day = now.strftime("%A")    # Tuesday
# day = now.day
# month = now.month
today_tuple = (now.month, now.day)
# print(today_tuple)

birthday_file = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in birthday_file.iterrows()}
# print(birthdays_dict)


if(today_tuple in birthdays_dict):
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
    # TLS: transport layer security, secures connection
        connection.starttls()
        connection.login(user= my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
    


