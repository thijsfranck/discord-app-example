import argparse
import logging
import os

import discord
from dotenv import load_dotenv

from .client import client

# Parse command-line arguments to configure the application.
parser = argparse.ArgumentParser(
    prog="python -m discord_app_example",
    description="Run the Discord bot application",
    epilog="For more information, see the documentation at https://discord-app-example.pages.dev/",
)
parser.add_argument(
    "--development",
    action="store_true",
    help="Run the application in development mode",
)
args = parser.parse_args()

# Determine the application mode. The default is production.
mode = os.getenv("MODE", "development" if args.development else "production")

# Load environment variables from a local .env file for development.
if mode == "development":
    load_dotenv()

# Determine the log level. The default is INFO.
log_level_name = os.getenv("LOG_LEVEL", "INFO")
log_level = logging.getLevelNamesMapping().get(log_level_name, logging.INFO)

# Continue with an empty token rather than raising an exception at this point. This allows
# discord.py to configure the logger and ensures a consistent output format.
token = os.getenv("DISCORD_TOKEN", "")

# Run the bot application with the specified token and log level.
try:
    client.run(
        token=token,
        log_level=log_level,
        root_logger=True,
    )
except discord.LoginFailure:
    logging.critical(
        "Invalid Discord token. Check the DISCORD_TOKEN environment variable.",
    )
