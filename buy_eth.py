"""Executing a buy order for Ethereum"""

import cbp_access

def eth_buy():
    trd1 = cbp_access.exchange.create_market_buy_order("ETH/USD", 0.001)
    return trd1
