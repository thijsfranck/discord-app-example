import logging

from discord import Client, Intents

client = Client(intents=Intents.default())
logger = logging.getLogger(__name__)


class DiscordAppExampleError(RuntimeError):
    """Base exception for the discord_app_example package."""


@client.event
async def on_ready() -> None:
    """Handle the on_ready event."""
    logger.info("%s has connected to Discord!", client.user)
