import logging

from discord import Client, Intents

client = Client(intents=Intents.default())

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler()],
)

logger = logging.getLogger(__name__)


@client.event
async def on_ready() -> None:
    """Handle the on_ready event."""
    logger.info("%s has connected to Discord!", client.user)
