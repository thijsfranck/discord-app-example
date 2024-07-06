import os

from dotenv import load_dotenv

from discord_app_example import client

if __name__ == "__main__":
    load_dotenv()
    client.run(os.getenv("DISCORD_TOKEN"))
