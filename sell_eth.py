""" Executing a sell order for Ethereum"""

import cbp_access

def eth_sell():
        trd2 = cbp_access.exchange.create_market_sell_order('ETH/USD', 0.01)
        return trd2

