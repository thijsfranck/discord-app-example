from discord import Client, Intents

client = Client(intents=Intents.default())


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")
