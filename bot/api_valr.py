import requests
import time
import hashlib
import hmac
import yaml
import ast


# --------------------------------------------------- CONFIGURATION -------------------------------------------------- #
def config(filepath):
    with open(filepath, "r") as f:
        return yaml.safe_load(f)


# --------------------------------------------------- GENERAL INFORMATION -------------------------------------------- #
"""VALR
EST: Include the following headers in each request:
X-VALR-API-KEY : your_key
X-VALR-SIGNATURE :your_secret
X-VALR-TIMESTAMP : The same timestamp used to generate the request signature"""

# --------------------------------------------------- CONSTANT VARIABLES --------------------------------------------- #
CONFIG_FILEPATH = "../config.yaml"
VALR_TICKER_SYMBOL = config(CONFIG_FILEPATH)['TRADING_PAIR']['VALR']
VALR_API_KEY = config(CONFIG_FILEPATH)['VALR_API']['KEY']
VALR_API_SECRET = config(CONFIG_FILEPATH)['VALR_API']['SECRET']

# --------------------------------------------------- FUNCTIONS ------------------------------------------------------ #


def sign_request(api_key_secret, timestamp, verb, path, body):
    """Signs the request payload using the api key secret
    api_key_secret - the api key secret
    timestamp - the unix timestamp of this request e.g. int(time.time()*1000)
    verb - Http verb - GET, POST, PUT or DELETE
    path - path excluding host name, e.g. '/v1/withdraw
    body - http request body as a string, optional
    """
    payload = "{}{}{}{}".format(timestamp, verb.upper(), path, body)
    message = bytearray(payload, 'utf-8')
    signature = hmac.new(bytearray(api_key_secret, 'utf-8'), message, digestmod=hashlib.sha512).hexdigest()
    return signature


def valr_order_book():
    try:
        endpoint_full = f'https://api.valr.com/v1/marketdata/{VALR_TICKER_SYMBOL}/orderbook'
        endpoint_ex_host_name = f'/v1/marketdata/{VALR_TICKER_SYMBOL}/orderbook'
        valr_timestamp = int(time.time() * 1000)
        signature = sign_request(
            api_key_secret=VALR_API_SECRET,
            timestamp=valr_timestamp,
            verb='GET',
            path=endpoint_ex_host_name,
            body=''
        )
        headers = {
            'X-VALR-API-KEY': VALR_API_KEY,
            'X-VALR-SIGNATURE': signature,
            'X-VALR-TIMESTAMP': str(valr_timestamp),
        }
        response = requests.get(url=endpoint_full, headers=headers)
        # print(response)
        # print(response.text)
        return response.json()
    except Exception as e:
        print(f"Error {e} occurred in getting the VALR order book, sleeping for 30 seconds before trying again")
        time.sleep(30)
        valr_order_book(currency_pair)


def get_valr_ticker():
    try:
        endpoint = f"https://api.valr.com/v1/public/{VALR_TICKER_SYMBOL}/marketsummary"
        result = requests.request("GET", endpoint, headers={}, data={}).text
        # print(result)
        return ast.literal_eval(result)

    except Exception as e:
        print(f"Error {e} occurred in get_luno_ticker, sleeping for 30 seconds before trying again")
        time.sleep(30)
        get_valr_ticker()


# def place_valr_simple_buy(payInCurrency, payAmount):
#     try:
#         endpoint_full = f"https://api.valr.com/v1/simple/{VALR_TICKER_SYMBOL}/quote"
#         endpoint_ex_host_name = f"/v1/simple/{VALR_TICKER_SYMBOL}/quote"
#         valr_timestamp = int(time.time() * 1000)
#         signature = sign_request(
#             api_key_secret=VALR_API_SECRET,
#             timestamp=valr_timestamp,
#             verb='GET',
#             path=endpoint_ex_host_name
#         )
#         headers = {
#             'X-VALR-API-KEY': VALR_API_KEY,
#             'X-VALR-SIGNATURE': signature,
#             'X-VALR-TIMESTAMP': str(valr_timestamp),
#         }
#         body = {
#             "payInCurrency": payInCurrency,
#             "payAmount": payAmount,
#             "side": "BUY"
#         }
#         response = requests.get(url=endpoint_full, headers=headers, body=body)
#         return response.json()
#     except Exception as e:
#         print(f"Exception {e} has occured\nNotifying OWNER and shutting down program")
#         return False


def place_valr_simple_sell(amount):
    # try:
        endpoint_full = f"https://api.valr.com/v1/simple/{VALR_TICKER_SYMBOL}/quote"
        endpoint_ex_host_name = f"/v1/simple/{VALR_TICKER_SYMBOL}/quote"
        valr_timestamp = int(time.time() * 1000)
        body = {
            "payInCurrency": "BTC",
            "payAmount": amount,
            "side": "SELL"
        }
        signature = sign_request(
            api_key_secret=VALR_API_SECRET,
            timestamp=valr_timestamp,
            verb='POST',
            path=endpoint_ex_host_name,
            body=body
        )
        headers = {
            'X-VALR-API-KEY': VALR_API_KEY,
            'X-VALR-SIGNATURE': signature,
            'X-VALR-TIMESTAMP': str(valr_timestamp),
        }
        response = requests.post(url=endpoint_full, headers=headers, params=body)
        return response.json()
    # except Exception as e:
    #     print(f"Exception: {e}\nNotifying OWNER and shutting down program")
    #     return False


# --------------------------------------------------- TESTING -------------------------------------------------------- #
# order_book(VALR_TICKER_SYMBOL)
# place_valr_simple_sell(amount="1000")
# time.sleep(1)
print(place_valr_simple_sell(amount="1000"))
