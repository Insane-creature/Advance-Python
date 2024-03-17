import smtplib

my_email = "anshikasoni323@gmail.com"
password = "znexlybeihcnsruv"

with smtplib.SMTP("smtp.gmail.com") as connection:
    # TLS: transport layer security, secures connection
    connection.starttls()
    connection.login(user= my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="anshikasoni357@gmail.com", 
        msg="Subject:Hi there!\n\nThis is mail body"
    )



