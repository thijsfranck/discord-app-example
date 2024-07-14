import logging
import os

import discord
from dotenv import load_dotenv

from discord_app_example import DiscordAppExampleError, client

# Load the environment variables from the .env file. If the file does not exist, this does nothing.
load_dotenv()

# Determine the log level. The default is INFO.
log_level_name = os.getenv("LOG_LEVEL", "INFO")
log_level = logging.getLevelNamesMapping().get(log_level_name, logging.INFO)

# Retrieve the Discord token. If the token is not set, continue with an empty token rather than,
# for example, raising an exception. This allows discord.py to configure the root logger before the
# token is validated, ensuring a consistent log output format no matter the outcome.
token = os.getenv("DISCORD_TOKEN", "")

# Run the bot application. Handle any errors raised by the application here.
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
except (discord.DiscordException, DiscordAppExampleError) as e:
    logging.critical(
        "An fatal error occurred while running the bot.",
        exc_info=e,
    )
