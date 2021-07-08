LUNO_BTC_AMT = '1'
LUNO_ZAR_AMT = '0'
VALR_BTC_AMT = '1'
VALR_ZAR_AMT = '10000'
NEXT_BUY_ON_VAL = 'v'
SPREAD_V_REQUIRED_SPREAD_VAL = '[]'

LUNO_BTC = 'data/luno_btc'
LUNO_ZAR = 'data/luno_zar'
VALR_BTC = 'data/valr_btc'
VALR_ZAR = 'data/valr_zar'
TRADE_TRACKER = 'data/trade_tracker'
NEXT_BUY_ON = 'data/next_buy_on'
SPREAD_V_REQUIRED_SPREAD = 'data/spread_v_required_spread'

amounts = [LUNO_BTC_AMT, LUNO_ZAR_AMT, VALR_BTC_AMT, VALR_ZAR_AMT, NEXT_BUY_ON_VAL, SPREAD_V_REQUIRED_SPREAD_VAL]
accounts = [LUNO_BTC, LUNO_ZAR, VALR_BTC, VALR_ZAR, NEXT_BUY_ON, SPREAD_V_REQUIRED_SPREAD]
null_accounts = [TRADE_TRACKER]

for n in range(6):
    with open(accounts[n], 'w') as file:
        file.write(amounts[n])
for item in null_accounts:
    with open(item, 'r+') as file:
        file.truncate(0)
print('Reset Complete')
