"""Defining a function to get the USD balance in coinbase pro"""

import cbp_access

usdBal = cbp_access.exchange.fetch_balance()


def curr_bal_usd():
    return usdBal['total']['USD']


print(curr_bal_usd())
