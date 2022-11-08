import discord
import credentials
from discord_client import DiscordClient

if __name__ == "__main__":
    discord_client = DiscordClient()
    discord_client.run(credentials.get_discord_token())