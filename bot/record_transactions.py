
LUNO_BTC = 'data/luno_btc'
LUNO_ZAR = 'data/luno_zar'
VALR_BTC = 'data/valr_btc'
VALR_ZAR = 'data/valr_zar'

# ------------------------------------------------------ LOW LEVEL FUNCTIONS ----------------------------------------- #


def update_balance(operation, account, amount):
    """
    operation;  'debit'/'credit'
    account; see constant variable set in main
    amount; float/int
    """
    with open(account, 'r') as file:
        balance = float(file.read())
    if operation == 'credit':
        new_balance = str(balance + amount)
    elif operation == 'debit':
        new_balance = str(balance - amount)
    with open(account, 'w') as new_file:
        new_file.write(new_balance)

# ------------------------------------------------------ MID LEVEL FUNCTIONS ----------------------------------------- #


def buy_valr(zar_amount, price):
    btc_amount = float(zar_amount) / float(price)
    update_balance('credit', VALR_BTC, btc_amount)
    update_balance('debit', VALR_ZAR, zar_amount)


def sell_valr(zar_amount, price):
    btc_amount = float(zar_amount) / float(price)
    update_balance('debit', VALR_BTC, btc_amount)
    update_balance('credit', VALR_ZAR, zar_amount)


def buy_luno(zar_amount, price):
    btc_amount = float(zar_amount) / float(price)
    update_balance('credit', LUNO_BTC, btc_amount)
    update_balance('debit', LUNO_ZAR, zar_amount)


def sell_luno(zar_amount, price):
    btc_amount = float(zar_amount) / float(price)
    update_balance('debit', LUNO_BTC, btc_amount)
    update_balance('credit', LUNO_ZAR, zar_amount)

# ------------------------------------------------------ HIGH LEVEL FUNCTIONS ---------------------------------------- #
