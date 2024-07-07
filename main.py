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

    Note
    ----
    Let discord.py configure the root logger to ensure consistently formatted logs across the app.
    """
    load_dotenv()

    # Passing an empty token will raise a discord.LoginFailure exception.
    token = os.getenv("DISCORD_TOKEN", "")

    try:
        client.run(
            token=token,
            root_logger=True,
            log_level=logging.INFO,
        )
    except discord.LoginFailure:
        logging.critical(
            "Invalid Discord token. Check the DISCORD_TOKEN environment variable.",
        )


if __name__ == "__main__":
    main()
