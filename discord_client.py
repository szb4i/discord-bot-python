import discord
from configuration import *
from binance.enums import *
from execute import Execute

class DiscordClient(discord.Client):
    def __init__(self):
        self.execute = Execute()

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        symbol = TRADE_SYMBOL
        side = SIDE_BUY
        direction = 'long'
        if SIDE_BUY == side and 'long' == direction:
            self.execute.open_long(symbol)
        elif SIDE_SELL == side and 'long' == direction:
            self.execute.close_long(symbol)
        elif SIDE_SELL == side and 'short' == direction:
            self.execute.open_short(symbol)
        elif SIDE_BUY == side and 'short' == direction:
            self.execute.close_short(symbol)
