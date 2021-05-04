import smtplib
import random
import datetime as dt

with open("quotes.txt") as quotes:
    quote = random.choice(quotes.readlines())

if dt.datetime.now().weekday() == 1:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Motivation Quote\n\n{quote}"
        )
