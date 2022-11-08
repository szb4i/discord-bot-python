import discord
from configuration import *
from binance.enums import *
from execute import Execute
from configuration import *
import credentials

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        symbol = TRADE_SYMBOL
        side = SIDE_BUY
        direction = 'long'
        if SIDE_BUY == side and 'long' == direction:
            execute.open_long(symbol)
        elif SIDE_SELL == side and 'long' == direction:
            execute.close_long(symbol)
        elif SIDE_SELL == side and 'short' == direction:
            execute.open_short(symbol)
        elif SIDE_BUY == side and 'short' == direction:
            execute.close_short(symbol)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
execute = Execute()
client.run(credentials.get_discord_token())