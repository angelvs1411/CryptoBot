"""Using the tradingview-ta package to get ethereum data from binance in 15 minute intervals"""

from tradingview_ta import TA_Handler, Interval

handler = TA_Handler(
    symbol="ETHUSD",
    screener="crypto",
    exchange="binance",
    interval=Interval.INTERVAL_15_MINUTES
)

analysis = handler.get_analysis()



