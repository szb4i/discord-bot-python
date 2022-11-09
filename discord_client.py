import discord
from binance.enums import *
from configuration import *
from services.binance_service import BinanceService

class DiscordClient(discord.Client):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.message_content = True
        discord.Client.__init__(self, intents=intents)
        self.binance_service = BinanceService()

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        symbol = TRADE_SYMBOL
        side = SIDE_BUY
        direction = 'long'
        if SIDE_BUY == side and 'long' == direction:
            self.binance_service.open_long(symbol)
        elif SIDE_SELL == side and 'long' == direction:
            self.binance_service.close_long(symbol)
        elif SIDE_SELL == side and 'short' == direction:
            self.binance_service.open_short(symbol)
        elif SIDE_BUY == side and 'short' == direction:
            self.binance_service.close_short(symbol)