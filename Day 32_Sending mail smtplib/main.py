# import smtplib

# my_email = "anshikasoni323@gmail.com"
# password = "znexlybeihcnsruv"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # TLS: transport layer security, secures connection
#     connection.starttls()
#     connection.login(user= my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="anshikasoni357@gmail.com", 
#         msg="Subject:Hi there!\n\nThis is mail body"
#     )

import datetime as dt
# module importing as dt

# print(dt.datetime.now()) # module.class - datetime is class of module dt
now = dt.datetime.now()
print(now.strftime("%A"))

