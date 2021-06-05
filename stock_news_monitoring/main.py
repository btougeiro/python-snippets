import requests
from twilio.rest import Client

STOCK_NAME = "<your_stock_name_here>"  # e.g. TSLA for Tesla
COMPANY_NAME = "<your_company_name_here>"  # e.g. "Tesla Inc"

STOCK_API_KEY = "<your_api_key_here>"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)

stock_price = [(key, value) for (key, value) in response.json()["Time Series (Daily)"].items()]

yesterday_stock_price = stock_price[0]
yesterday_closing_stock_price = float(yesterday_stock_price[1]["4. close"])

day_before_yesterday_stock_price = stock_price[1]
day_before_yesterday_closing_stock_price = float(day_before_yesterday_stock_price[1]["4. close"])

diff = round(yesterday_closing_stock_price - day_before_yesterday_closing_stock_price, 2)
up_down = None
if diff > 0:
    up_down = "⬆"
else:
    up_down = "⬇"

percentage = round(((diff / yesterday_closing_stock_price) * 100), 2)

NEWS_API_KEY = "<your_api_key_here>"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

if abs(percentage) > 4:

    parameters = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    response = requests.get(url=NEWS_ENDPOINT, params=parameters)
    articles = response.json()["articles"]
    three_articles = articles[:3]
    fmt_articles = [
        f"{STOCK_NAME}: {up_down}{percentage}% \nHeadline: {article['title']} \nBrief: {article['description']}"
        for article in three_articles
    ]

    # twilio id and token
    twilio_account_sid = "<your_account_sid_here>"
    twilio_auth_token = "<your_api_key_here>"

    client = Client(twilio_account_sid, twilio_auth_token)
    for msg in fmt_articles:
        message = client.messages.create(
            body=msg,
            from_="<your_twilio_number_here>",
            to="<your_personal_number_here>"
        )
