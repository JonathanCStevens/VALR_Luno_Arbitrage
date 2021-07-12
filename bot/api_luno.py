import requests
import base64
from luno_python.client import Client
import time
import yaml


# --------------------------------------------------- CONFIGURATION -------------------------------------------------- #
def config(filepath):
    with open(filepath, "r") as f:
        return yaml.safe_load(f)


# --------------------------------------------------- CONSTANT VARIABLES --------------------------------------------- #
CONFIG_FILEPATH = "./config.yaml"

END_POINT = "https://api.luno.com"

LUNO_API_KEY = config(CONFIG_FILEPATH)['LUNO_API']['KEY']
LUNO_API_SECRET = config(CONFIG_FILEPATH)['LUNO_API']['SECRET']
LUNO_TICKER_SYMBOL = config(CONFIG_FILEPATH)['TRADING_PAIR']['LUNO']

# --------------------------------------------------- OBJECT CREATION ------------------------------------------------ #
client = Client(api_key_id=LUNO_API_KEY, api_key_secret=LUNO_API_SECRET)

# --------------------------------------------------- FUNCTIONS ------------------------------------------------------ #


def luno_order_book(currency_pair):
    try:
        endpoint_full = f"https://api.luno.com/api/1/orderbook_top?pair={currency_pair}"
        headers = {}
        response = requests.get(url=endpoint_full, headers = headers)
        return response.json()
        
    except Exception as e:
        print(f"Error {e} occurred in getting the Luno order book, sleeping for 30 seconds before trying again")
        time.sleep(30)
        luno_order_book(currency_pair)


def get_luno_ticker():
    try:
        result = client.get_ticker(LUNO_TICKER_SYMBOL)
        # print(result)
        return result

    except Exception as e:
        print(f"Error {e} occurred in get_ticker, sleeping for 30 seconds before trying again")
        time.sleep(30)
        get_luno_ticker()
