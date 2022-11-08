from binance.enums import *
from binance.client import Client
import credentials
from configuration import *

class Execute():
    def __init__(self):
        self.client=Client(credentials.get_binance_key(), credentials.get_binance_secret_key())

    def open_long(self, symbol):
        self.client.futures_change_leverage(symbol=symbol, leverage=LEVERAGE)
        order = self.client.futures_create_order(symbol=symbol, side=SIDE_BUY, type=FUTURE_ORDER_TYPE_MARKET, quantity=TRADE_QUANTITY, isIsolated=True)
        print('action: long opened')
        print(order)

    def close_long(self, symbol):
        self.client.futures_change_leverage(symbol=symbol, leverage=LEVERAGE)
        order = self.client.futures_create_order(symbol=symbol, side=SIDE_SELL, type=FUTURE_ORDER_TYPE_MARKET, quantity=TRADE_QUANTITY, isIsolated=True)
        print('action: long closed')
        print(order)

    def open_short(self, symbol):
        self.client.futures_change_leverage(symbol=symbol, leverage=LEVERAGE)
        order = self.client.futures_create_order(symbol=symbol, side=SIDE_SELL, type=FUTURE_ORDER_TYPE_MARKET, quantity=TRADE_QUANTITY, isIsolated=True)
        print('action: short opened')
        print(order)

    def close_short(self, symbol):
        self.client.futures_change_leverage(symbol=symbol, leverage=LEVERAGE)
        order = self.client.futures_create_order(symbol=symbol, side=SIDE_BUY, type=FUTURE_ORDER_TYPE_MARKET, quantity=TRADE_QUANTITY, isIsolated=True)
        print('action: short closed')
        print(order)