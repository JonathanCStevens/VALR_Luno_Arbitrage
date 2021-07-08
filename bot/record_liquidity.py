from liquidity_screening import luno_check_bids, luno_check_asks, valr_check_bids, valr_check_asks
import api_valr as vapi
import api_luno as lapi
import time

while True:
    lta = lapi.get_luno_ticker()['ask'].split('.')[0]
    ltb = lapi.get_luno_ticker()['bid'].split('.')[0]
    vta = vapi.get_valr_ticker()['askPrice']
    vtb = vapi.get_valr_ticker()['bidPrice']
    loa = luno_check_asks(1000, lapi.luno_order_book("XBTZAR"))
    lob = luno_check_bids(1000, lapi.luno_order_book("XBTZAR"))
    voa = valr_check_asks(1000, vapi.valr_order_book("BTCZAR"))
    vob = valr_check_bids(1000, vapi.valr_order_book("BTCZAR"))
    slbv = float(ltb) - float(vta)
    blsv = float(vtb) - float(lta)
    print(f"lta = {lta}         loa = {loa}\n"
          f"ltb = {ltb}         lob = {loa}\n"
          f"vta = {vta}         voa = {voa}\n"
          f"vtb = {vtb}         vob = {vob}\n"
          f"sell luno --> buy valr = {slbv}\n"
          f"sell valr --> buy luno = {blsv}")
    time.sleep(1)
