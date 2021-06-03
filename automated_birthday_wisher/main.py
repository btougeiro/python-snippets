from datetime import datetime
import pandas
import random
import smtplib as smtp

email = None
password = None
host = None
port = None
email_subject = "Happy Birthday!"
sender = None

now = datetime.now()
today_tuple = (now.month, now.day)

birthday_file = pandas.read_csv("birthdays.csv")

birthdays_dict = { (data_row.month, data_row.day):data_row for _, data_row in birthday_file.iterrows() }

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])
        content = content.replace("[SENDER]", sender)

    with smtp.SMTP(host=host, port=port) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=birthday_person["email"], msg=f"Subject:{email_subject}\n\n{content}")
