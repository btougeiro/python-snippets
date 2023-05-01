import smtplib as smtp
import datetime as dt
import random

host = None
port = None
email = None
password = None

now = dt.datetime.now()
weekday = now.weekday()

if weekday in range(0, 5):
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtp.SMTP(host=host, port=port) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=email, msg=f"Subject:Motivational Message\n\n{quote}")
