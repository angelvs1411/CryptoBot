""" Using the tradingview-ta package to get the current RSI value for ETH"""

import ta

analysis = ta.handler.get_analysis()


def get_rsi():
    rsi_eth = analysis.indicators['RSI']
    return rsi_eth

print(get_rsi())

