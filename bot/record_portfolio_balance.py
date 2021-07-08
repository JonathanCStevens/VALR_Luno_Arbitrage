import ast
from datetime import datetime as dt

# --------------------------------------------------- CONSTANT VARIABLES --------------------------------------------- #

LUNO_BTC = 'data/luno_btc'
LUNO_ZAR = 'data/luno_zar'
VALR_BTC = 'data/valr_btc'
VALR_ZAR = 'data/valr_zar'

# --------------------------------------------------- FUNCTIONS ------------------------------------------------------ #


def get_portfolio_balances(valr_ticker, luno_ticker, spread, profit):
    with open(LUNO_BTC, 'r') as file:
        luno_btc_amt = file.read()
    with open(LUNO_ZAR, 'r') as file:
        luno_zar_amt = file.read()
    with open(VALR_BTC, 'r') as file:
        valr_btc_amt = file.read()
    with open(VALR_ZAR, 'r') as file:
        valr_zar_amt = file.read()
    total_btc = float(luno_btc_amt) + float(valr_btc_amt)
    total_zar = float(luno_zar_amt) + float(valr_zar_amt)
    balance_dict = {
        "time": dt.now(),
        "l_btc": luno_btc_amt,
        "l_zar": luno_zar_amt,
        "v_btc": valr_btc_amt,
        "v_zar": valr_zar_amt,
        "total_btc": total_btc,
        "total_zar": total_zar,
        "l_btc_bid_price": luno_ticker['bid'].split('.')[0],
        "l_btc_ask_price": luno_ticker['ask'].split('.')[0],
        "v_btc_bid_price": valr_ticker['bidPrice'],
        "v_btc_ask_price": valr_ticker['askPrice'],
        "l_spread": str(int(luno_ticker['ask'].split('.')[0]) - int(luno_ticker['bid'].split('.')[0])),
        "v_spread": str(int(valr_ticker['askPrice']) - int(valr_ticker['bidPrice'])),
        "spread_on_trade": spread,
        "profit": profit,
    }
    try:
        with open('../data/trade_tracker', 'r') as file:
            result_list = ast.literal_eval(file.read())
    except Exception as e:
        result_list = []
        print('error in check portfolio balance')

    result_list.append(balance_dict)
    with open('../data/trade_tracker', 'w') as file:
        file.write(str(result_list))


def spread_tracker(spread, required_spread, current_buy):
    with open('../data/spread_v_required_spread', 'r') as file:
        data = ast.literal_eval(file.read())

    new_data = {"spread": str(spread), "required_spread": str(required_spread), "exchange": current_buy}
    data.append(new_data)
    with open('../data/spread_v_required_spread', 'w') as file:
        file.write(str(data))
