import record_transactions as tt
from bot import liquidity_screening as idp
from datetime import datetime as dt
import time
import api_valr as vapi
import api_luno as lapi

# --------------------------------------------------- CONSTANT VARIABLES --------------------------------------------- #
LUNO_BTC = 'data/luno_btc'
LUNO_ZAR = 'data/luno_zar'
VALR_BTC = 'data/valr_btc'
VALR_ZAR = 'data/valr_zar'

# --------------------------------------------------- VARIABLE VARIABLES --------------------------------------------- #
trading_zar_amt = 1000
luno_fee = 0.001
valr_fee = 0.001
session_profit = 0
# --------------------------------------------------- FUNCTIONS ------------------------------------------------------ #
print('program running')
next_buy_on = 'l'
n = 0
while True:
    try:

        if next_buy_on == 'l':
            vob = vapi.valr_order_book("BTCZAR")
            lob = lapi.luno_order_book("XBTZAR")
            vb = idp.valr_check_bids(trading_zar_amt, vob)
            la = idp.luno_check_asks(trading_zar_amt, lob)
            required_spread = 0.002 * la['wa_ask_price']
            spread = vb['wa_bid_price'] - la['wa_ask_price']
            # cpb.spread_tracker(spread=spread, required_spread=required_spread, current_buy=next_buy_on)
            if vb['zar_amount'] > trading_zar_amt and la['zar_amount'] > trading_zar_amt:
                if spread > required_spread:
                    profit = trading_zar_amt * (spread / vb['wa_bid_price']) - (trading_zar_amt * (luno_fee + valr_fee))
                    session_profit += profit
                    print(f'The VALR selling price is higher than the Luno buying price by R{spread} V --> L '
                          f'profit: R{profit} at {dt.now().strftime("%Y/%M/%d %H:%M:%S")} session profit: {session_profit}')
                    # paper trading commands
                    tt.buy_luno(trading_zar_amt, la['wa_ask_price'])
                    tt.sell_valr(trading_zar_amt, vb['wa_bid_price'])
                    # variable update
                    n += 1
                    if n == 10:
                        next_buy_on = 'v'
                        n = 0

        if next_buy_on == 'v':
            vob = vapi.valr_order_book("BTCZAR")
            lob = lapi.luno_order_book("BTCZAR")
            lb = idp.luno_check_bids(trading_zar_amt, lob)
            va = idp.valr_check_asks(trading_zar_amt, vob)
            required_spread = 0.002 * va['wa_ask_price']
            spread = lb['wa_bid_price'] - va['wa_ask_price']
            # cpb.spread_tracker(spread=spread, required_spread=required_spread, current_buy=next_buy_on)
            if lb['zar_amount'] > trading_zar_amt and va['zar_amount'] > trading_zar_amt:
                if spread > required_spread:
                    profit = trading_zar_amt * (spread / lb['wa_bid_price']) - (trading_zar_amt * (luno_fee + valr_fee))
                    session_profit += profit
                    print(f'The Luno selling price is higher than the VALR buying price by R{spread} L --> V '
                          f'profit: R{profit} at {dt.now().strftime("%Y/%M/%d %H:%M:%S")} session profit: {session_profit}')
                    # paper trading commands
                    tt.buy_valr(trading_zar_amt, va['wa_ask_price'])
                    tt.sell_luno(trading_zar_amt, lb['wa_bid_price'])
                    # variable update
                    n += 1
                    if n == 10:
                        next_buy_on = 'l'
                        n = 0

        time.sleep(2)

    except Exception as e:
        print(e)
        time.sleep(20)
        if next_buy_on == 'l':
            vob = vapi.valr_order_book("BTCZAR")
            lob = lapi.luno_order_book("BTCZAR")
            vb = idp.valr_check_bids(trading_zar_amt, vob)
            la = idp.luno_check_asks(trading_zar_amt, lob)
            required_spread = 0.002 * la['wa_ask_price']
            spread = vb['wa_bid_price'] - la['wa_ask_price']
            # cpb.spread_tracker(spread=spread, required_spread=required_spread, current_buy=next_buy_on)
            if vb['zar_amount'] > trading_zar_amt and la['zar_amount'] > trading_zar_amt:
                if spread > required_spread:
                    profit = trading_zar_amt * (spread / vb['wa_bid_price']) - (trading_zar_amt * (luno_fee + valr_fee))
                    session_profit += profit
                    print(f'The VALR selling price is higher than the Luno buying price by R{spread} V --> L '
                          f'profit: R{profit} at {dt.now().strftime("%Y/%M/%d %H:%M:%S")} session profit: {session_profit}')
                    # paper trading commands
                    tt.buy_luno(trading_zar_amt, la['wa_ask_price'])
                    tt.sell_valr(trading_zar_amt, vb['wa_bid_price'])
                    # variable update
                    n += 1
                    if n == 10:
                        next_buy_on = 'v'
                        n = 0

        if next_buy_on == 'v':
            vob = vapi.valr_order_book("BTCZAR")
            lob = lapi.luno_order_book("XBTZAR")
            lb = idp.luno_check_bids(trading_zar_amt, lob)
            va = idp.valr_check_asks(trading_zar_amt, vob)
            required_spread = 0.002 * va['wa_ask_price']
            spread = lb['wa_bid_price'] - va['wa_ask_price']
            # cpb.spread_tracker(spread=spread, required_spread=required_spread, current_buy=next_buy_on)
            if lb['zar_amount'] > trading_zar_amt and va['zar_amount'] > trading_zar_amt:
                if spread > required_spread:
                    profit = trading_zar_amt * (spread / lb['wa_bid_price']) - (trading_zar_amt * (luno_fee + valr_fee))
                    session_profit += profit
                    print(f'The Luno selling price is higher than the VALR buying price by R{spread} L --> V '
                          f'profit: R{profit} at {dt.now().strftime("%Y/%M/%d %H:%M:%S")} session profit: {session_profit}')
                    # paper trading commands
                    tt.buy_valr(trading_zar_amt, va['wa_ask_price'])
                    tt.sell_luno(trading_zar_amt, lb['wa_bid_price'])
                    # variable update
                    n += 1
                    if n == 10:
                        next_buy_on = 'l'
                        n = 0

    time.sleep(2)

# --------------------------------------------------- COMMENTS ------------------------------------------------------- #
