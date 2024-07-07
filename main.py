import logging
import os

import discord
from dotenv import load_dotenv

from discord_app_example import client

if __name__ == "__main__":
    load_dotenv()

    TOKEN = os.getenv("DISCORD_TOKEN", "")

    try:
        # Apply the discord.py logger configuration to the root logger to ensure well formatted logs
        client.run(
            token=TOKEN,
            root_logger=True,
            log_level=logging.INFO,
        )
    except discord.LoginFailure:
        logging.critical(
            "Invalid Discord token. Check the DISCORD_TOKEN environment variable.",
        )
