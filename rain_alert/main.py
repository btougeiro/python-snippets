import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os

# open weather map credentials and api
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
OWM_Endpoint_Api_Key = os.environ.get("OWM_ENDPOINT_API_KEY")

# twilio account and api
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

parameters = {
    "lat": "",
    "lon": "",
    "appid": OWM_Endpoint_Api_Key,
    "exclude": "current,minutely,daily"
}

weather_map_response = requests.get(url=OWM_Endpoint, params=parameters)
weather_map_response.raise_for_status()
weather_data = weather_map_response.json()

weather_slice = weather_data["hourly"][:12]

will_rain = False
for weather in weather_slice:
    if weather["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.environ["https_proxy"]}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔.",
        from_="",
        to=""
    )
