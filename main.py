import os
from dotenv import dotenv_values
from discord.ext import commands

config = dotenv_values('.secret_keys')
BOT_KEY = config['BOT_KEY']
OWNERS = config['OWNERS']

client = commands.Bot(command_prefix="--")

@client.command()
async def loads(ctx, extension):
    client.load_extension(f"cogs.{extension}")


@client.command()
async def unloads(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(BOT_KEY)
