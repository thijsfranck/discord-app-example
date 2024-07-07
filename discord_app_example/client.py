import logging

from discord import Client, Intents

client = Client(intents=Intents.default())
logger = logging.getLogger(__name__)


@client.event
async def on_ready() -> None:
    """Handle the on_ready event."""
    logger.info("%s has connected to Discord!", client.user)
