# import valr_api as vapi  # //uncomment when testing in this file//
# import luno_api as lapi  # //uncomment when testing in this file//

# --------------------------------------------------- LUNO ----------------------------------------------------------- #


def luno_check_asks(trading_zar_amount, order_book):
    # order_book = lapi.order_book(currency_pair="XBTZAR")  # //uncomment when testing in this file//
    asks = order_book["asks"]
    zar_amount_first = float(asks[0]['volume']) * float(asks[0]['price'])
    if zar_amount_first > trading_zar_amount * 1.5:  # 1.5 is the margin
        return {'zar_amount': zar_amount_first, 'wa_ask_price': float(asks[0]['price']), 'num_asks_for_wa': 1}

    # top 2 weighted average
    else:
        # create lists
        price_list = []
        quantity_list = []
        zar_amount_list = []
        total_btc_quantity = 0
        total_zar_amount = 0
        for ask in asks[0:5]:
            price_list.append(float(ask['price']))
            quantity_list.append(float(ask['volume']))
            zar_amount_list.append(float(ask['price']) * float(ask['volume']))
            total_btc_quantity += float(ask['volume'])
            total_zar_amount += float(ask['price']) * float(ask['volume'])
        # create wac
        WAC_top_5 = 0
        for n in range(5):
            WAC_top_5 += (quantity_list[n] / total_btc_quantity) * price_list[n]

        # print(price_list)
        # print(quantity_list)
        # print(zar_amount_list)
        return {'zar_amount': total_zar_amount, 'wa_ask_price': WAC_top_5, 'num_asks_for_wa': 5}


def luno_check_bids(trading_zar_amount, order_book):
    # order_book = lapi.order_book(currency_pair="XBTZAR")  # //uncomment when testing in this file//
    bids = order_book["bids"]
    zar_amount_first = float(bids[0]['volume']) * float(bids[0]['price'])
    if zar_amount_first > trading_zar_amount * 1.5:  # 1.5 is the margin
        return {'zar_amount': zar_amount_first, 'wa_bid_price': float(bids[0]['price']), 'num_bids_for_wa': 1}

    # top 2 weighted average
    else:
        # create lists
        price_list = []
        quantity_list = []
        zar_amount_list = []
        total_btc_quantity = 0
        total_zar_amount = 0
        for bid in bids[0:5]:
            price_list.append(float(bid['price']))
            quantity_list.append(float(bid['volume']))
            zar_amount_list.append(float(bid['price']) * float(bid['volume']))
            total_btc_quantity += float(bid['volume'])
            total_zar_amount += float(bid['price']) * float(bid['volume'])
        # create wac
        WAC_top_5 = 0
        for n in range(5):
            WAC_top_5 += (quantity_list[n] / total_btc_quantity) * price_list[n]

        # print(price_list)
        # print(quantity_list)
        # print(zar_amount_list)
        return {'zar_amount': total_zar_amount, 'wa_bid_price': WAC_top_5, 'num_bids_for_wa': 5}


# --------------------------------------------------- VALR ----------------------------------------------------------- #


def valr_check_asks(trading_zar_amount, order_book):
    # order_book = vapi.order_book(currency_pair="BTCZAR")  # //uncomment when testing in this file//
    asks = order_book["Asks"]
    zar_amount_first = float(asks[0]['quantity']) * float(asks[0]['price'])
    if zar_amount_first > trading_zar_amount * 1.5:  # 1.5 is the margin
        return {'zar_amount': zar_amount_first, 'wa_ask_price': float(asks[0]['price']), 'num_asks_for_wa': 1}

    # top 2 weighted average
    else:
        # create lists
        price_list = []
        quantity_list = []
        zar_amount_list = []
        total_btc_quantity = 0
        total_zar_amount = 0
        for ask in asks[0:5]:
            price_list.append(float(ask['price']))
            quantity_list.append(float(ask['quantity']))
            zar_amount_list.append(float(ask['price']) * float(ask['quantity']))
            total_btc_quantity += float(ask['quantity'])
            total_zar_amount += float(ask['price']) * float(ask['quantity'])
        # create wac
        WAC_top_5 = 0
        for n in range(5):
            WAC_top_5 += (quantity_list[n] / total_btc_quantity) * price_list[n]

        # print(price_list)
        # print(quantity_list)
        # print(zar_amount_list)
        return {'zar_amount': total_zar_amount, 'wa_ask_price': WAC_top_5, 'num_asks_for_wa': 5}


def valr_check_bids(trading_zar_amount, order_book):
    # order_book = vapi.order_book(currency_pair="BTCZAR")  # //uncomment when testing in this file//
    # print(order_book)
    bids = order_book["Bids"]
    zar_amount_first = float(bids[0]['quantity']) * float(bids[0]['price'])
    if zar_amount_first > trading_zar_amount * 1.5:  # 1.5 is the margin
        return {'zar_amount': zar_amount_first, 'wa_bid_price': float(bids[0]['price']), 'num_bids_for_wa': 1}

    # top 2 weighted average
    else:
        # create lists
        price_list = []
        quantity_list = []
        zar_amount_list = []
        total_btc_quantity = 0
        total_zar_amount = 0
        for bid in bids[0:5]:
            price_list.append(float(bid['price']))
            quantity_list.append(float(bid['quantity']))
            zar_amount_list.append(float(bid['price']) * float(bid['quantity']))
            total_btc_quantity += float(bid['quantity'])
            total_zar_amount += float(bid['price']) * float(bid['quantity'])
        # create wac
        WAC_top_5 = 0
        for n in range(5):
            WAC_top_5 += (quantity_list[n] / total_btc_quantity) * price_list[n]

        # print(price_list)
        # print(quantity_list)
        # print(zar_amount_list)
        return {'zar_amount': total_zar_amount, 'wa_bid_price': WAC_top_5, 'num_bids_for_wa': 5}


# --------------------------------------------------- TEST ----------------------------------------------------------- #

# print(gt()['bidPrice'])
# print(luno_check_bids(10000))
# print(valr_check_asks(900000))
#
# time.sleep(2)
#
# print(valr_check_bids(10000))
# print(luno_check_asks(10000))
