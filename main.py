import os

from dotenv import load_dotenv

from discord_app_example import client

if __name__ == "__main__":
    load_dotenv()

    TOKEN = os.getenv("DISCORD_TOKEN")

    if not TOKEN:
        message = "Discord bot token not found. Please set the DISCORD_TOKEN environment variable."
        raise ValueError(message)

    client.run(TOKEN)
