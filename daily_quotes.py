# import smtplib
#
mail = "testuserbob28@gmail.com"
password = "enzs grkq weto kpbd"
to_address = "testuserbob28@yahoo.com"
#
# with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
#     connection.starttls()
#     connection.login(user=mail,password=password)
#     connection.sendmail(
#         from_addr=mail,
#         to_addrs=to_address,
#         msg="Subject:Hello\n\nHi"
#     )
import datetime as dt
import random
import smtplib

now = dt.datetime.now()
with open("quotes.txt","r") as file:
    quotes = file.readlines()
random_quote = random.choice(quotes)
with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
    connection.starttls()
    connection.login(user=mail,password=password)
    connection.sendmail(
        from_addr=mail,
        to_addrs=mail,
        msg=f"Subject:QUOTE OF THE DAY!!!\n{random_quote}"
    )







