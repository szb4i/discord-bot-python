import discord
from configuration import *
import credentials
from discord_client import DiscordClient

if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True
    discord_client = DiscordClient(intents=intents)
    discord_client.run(credentials.get_discord_token())
