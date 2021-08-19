""" Authorization for Coinbase Pro API using the ccxt packages """

import ccxt
import config


exchange = ccxt.coinbasepro({
    'apiKey': config.CBP_API_KEY,
    'secret': config.CBP_SECRET_KEY,
    'password': config.CBP_PW
})
