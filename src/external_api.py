import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_exchange_rate(currency, amount):
    to = "RUB"
    froms = currency

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={froms}&amount={amount}"
    headers = {"apikey": os.getenv('API')}

    response = requests.get(url, headers=headers, data={})
    return response.json().get("result")
