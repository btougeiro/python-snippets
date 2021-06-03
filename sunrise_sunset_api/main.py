import requests
from datetime import datetime
import smtplib as smtp
import time

# api urls

SUNRISE_SUNSET_API_URL = "https://api.sunrise-sunset.org/json"
ISS_LOCATION_API_URL = "http://api.open-notify.org/iss-now.json"

# mail configuration

mail = None
password = None
host = None
port = None
mail_subject = "ISS Notification - Look Up"
content = "The ISS is above you in the sky."
sender = mail

# sunrise and sunset block

MY_LAT = None
MY_LNG = None

def is_night():
    parameters = { "lat": MY_LAT, "lng": MY_LNG, "formatted": 0 }
    response = requests.get(url=SUNRISE_SUNSET_API_URL, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

# iss notification block
def is_iss_overhead():
    response = requests.get(url=ISS_LOCATION_API_URL)
    response.raise_for_status()
    data = response.json()
    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LNG-5 <= iss_lng <= MY_LNG+5:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtp.SMTP(host=host, port=port) as connection:
            connection.starttls()
            connection.login(user=mail, password=password)
            connection.sendmail(from_addr=mail, to_addrs=mail, msg=f"Subject:{mail_subject}\n\n{content}")
