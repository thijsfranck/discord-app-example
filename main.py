import logging
import os

import discord
from dotenv import load_dotenv

from discord_app_example import client


def main() -> None:
    """
    Initialize and run the Discord bot application.

    Loads environment variables from a .env file if present in the root directory.

    Retrieves the Discord token from the `DISCORD_TOKEN` environment variable and attempts to start
    the client. If the token is missing or invalid, logs a critical message and exits.

    The log level can be set using the `LOG_LEVEL` environment variable. The default is `INFO`.

    Note
    ----
    Let discord.py configure the root logger to ensure consistently formatted logs across the app.
    """
    load_dotenv()

    # Passing an empty token will raise a discord.LoginFailure exception.
    token = os.getenv("DISCORD_TOKEN", "")

    log_level_name = os.getenv("LOG_LEVEL", "INFO")
    log_level = logging.getLevelNamesMapping().get(log_level_name, logging.INFO)

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


if __name__ == "__main__":
    main()
