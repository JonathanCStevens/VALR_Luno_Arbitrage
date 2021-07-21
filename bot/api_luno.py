import requests
import base64
import time
import yaml


# --------------------------------------------------- CONFIGURATION -------------------------------------------------- #
def config(filepath):
    with open(filepath, "r") as f:
        return yaml.safe_load(f)


# --------------------------------------------------- CONSTANT VARIABLES --------------------------------------------- #
CONFIG_FILEPATH = "../config.yaml"

END_POINT = "https://api.luno.com"

LUNO_API_KEY = config(CONFIG_FILEPATH)['LUNO_API']['KEY']
LUNO_API_SECRET = config(CONFIG_FILEPATH)['LUNO_API']['SECRET']
LUNO_TICKER_SYMBOL = config(CONFIG_FILEPATH)['TRADING_PAIR']['LUNO']

# --------------------------------------------------- LUNO AUTHENTICATION -------------------------------------------- #
client_id = LUNO_API_KEY
client_secret = LUNO_API_SECRET
encodedData = base64.b64encode(bytes(f"{client_id}:{client_secret}", "ISO-8859-1")).decode("ascii")
authorization_header_string = f"Authorization: Basic {encodedData}"

headers = {
    'Authorization': f'Basic {encodedData}',
}

get_balance_endpoint = "https://api.luno.com/api/1/balance"

# --------------------------------------------------- FUNCTIONS ------------------------------------------------------ #


def get_luno_order_book():
    try:
        order_book_endpoint_full = f"https://api.luno.com/api/1/orderbook_top?pair={LUNO_TICKER_SYMBOL}"
        response = requests.get(url=order_book_endpoint_full, headers=headers)
        return response.json()
    except Exception as e:
        print(f"Error {e} occurred in get_ticker, sleeping for 30 seconds before trying again")
        time.sleep(30)
        get_luno_order_book()


def get_luno_ticker():
    try:
        ticker_endpoint_full = "https://api.luno.com/api/1/ticker"
        parameters = {
            "pair": LUNO_TICKER_SYMBOL
        }
        response = requests.get(url=ticker_endpoint_full, headers=headers, params=parameters)
        return response.text

    except Exception as e:
        print(f"Error {e} occurred in get_ticker, sleeping for 30 seconds before trying again")
        time.sleep(30)
        get_luno_ticker()


def list_luno_trades():
    list_trades_endpoint = "https://api.luno.com/api/1/listtrades"
    parameters = {
        "pair": LUNO_TICKER_SYMBOL,
        "since": None,
        "before": None,
        "after_seq": None,
        "before_seq": None,
        "sort_desc": None,
        "limit": None,
    }
    response = requests.get(url=list_trades_endpoint, headers=headers, params=parameters)
    return response.text


# --------------------------------------------------- TESTING -------------------------------------------------------- #

print(get_luno_ticker())
print(get_luno_order_book())
print(list_luno_trades())
