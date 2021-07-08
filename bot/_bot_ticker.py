import record_transactions as tt
import record_portfolio_balance as cp
from datetime import datetime as dt
import api_valr
import api_luno
import yaml


# --------------------------------------------------- CONFIGURATION -------------------------------------------------- #
def config(filepath):
    with open(filepath, "r") as f:
        return yaml.safe_load(f)


# --------------------------------------------------- CONSTANT VARIABLES --------------------------------------------- #
LUNO_BTC = 'data/luno_btc'
LUNO_ZAR = 'data/luno_zar'
VALR_BTC = 'data/valr_btc'
VALR_ZAR = 'data/valr_zar'
CONFIG_FILEPATH = "./config.yaml"

# --------------------------------------------------- VARIABLE VARIABLES --------------------------------------------- #
trading_zar_amt = config(CONFIG_FILEPATH)['TRADING_INPUTS']['TRADING_AMOUNT']
luno_fee = config(CONFIG_FILEPATH)['FEES']['LUNO']
valr_fee = config(CONFIG_FILEPATH)['FEES']['VALR']
session_profit = 0

# --------------------------------------------------- FUNCTIONS ------------------------------------------------------ #
print('program running')
while True:
    lt = api_luno.get_luno_ticker()  # luno ticker
    vt = api_valr.get_valr_ticker()  # valr ticker

    with open('./data/next_buy_on', 'r') as file:  # checks which exchange should be bought from next
        next_buy_on = file.read()

    if next_buy_on == 'v':
        if float(vt['bidPrice']) - float(lt['ask']) > 1100:
            spread = float(vt['bidPrice']) - float(lt['ask'])
            profit = trading_zar_amt * (spread / float(vt["bidPrice"])) - (trading_zar_amt * (luno_fee + valr_fee))
            session_profit += profit
            print(f'The VALR selling price is higher than the Luno buying price by R{spread} V --> L '
                  f'profit: R{profit} at {dt.now().strftime("%Y/%M/%d %H:%M:%S")} session profit: {session_profit}')
            # paper trading commands
            tt.buy_luno(trading_zar_amt, lt['ask'])
            tt.sell_valr(trading_zar_amt, vt['bidPrice'])
            # variable update
            next_buy_on = 'l'
            cp.get_portfolio_balances(vt, lt, spread, profit)

    if next_buy_on == 'l':
        if float(lt['bid']) - float(vt['askPrice']) > 1100:
            spread = float(lt['bid']) - float(vt['askPrice'])
            profit = trading_zar_amt * (spread / float(lt["bid"])) - (trading_zar_amt * (luno_fee + valr_fee))
            session_profit += profit
            print(f'The Luno selling price is higher than the VALR buying price by R{spread} L --> V '
                  f'profit: R{profit} at {dt.now().strftime("%Y/%M/%d %H:%M:%S")} session profit: {session_profit}')
            # paper trading commands
            tt.buy_valr(trading_zar_amt, vt['askPrice'])
            tt.sell_luno(trading_zar_amt, lt['bid'])
            # variable update
            next_buy_on = 'v'
            cp.get_portfolio_balances(vt, lt, spread, profit)

    with open('./data/next_buy_on', 'w') as file:  # updates which exchange should be bought from next
        file.write(next_buy_on)

    # time.sleep(2)

# --------------------------------------------------- COMMENTS ------------------------------------------------------- #

# TODO: let the price difference parameters be automatically determined by the price of bitcoin

# record session profit:
# 12:00 - 6:45 R948

