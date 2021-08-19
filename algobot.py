""" Final Code"""

import usd_bal
import get_ethRSI
import buy_eth
import eth_bal
import sell_eth

rsi = get_ethRSI.get_rsi()
usd = usd_bal.curr_bal_usd()
eth = eth_bal.curr_bal_eth()


def b_trade():
    if (rsi <= 35) and (usd >= 3):
        print(buy_eth.eth_buy())
    else:
        print("Buy conditions not met")

def s_trade():
    if (rsi >= 70) and (eth >= 0.009):
        print(sell_eth.eth_sell())
    else:
        print("Sell conditions not met.")



b_trade()
s_trade()