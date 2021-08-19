"""Defining a function to get the ETH balance in coinbase pro"""

import cbp_access

ethBal = cbp_access.exchange.fetch_balance()


def curr_bal_eth():
    return ethBal['total']['ETH']


curr_bal_eth()
