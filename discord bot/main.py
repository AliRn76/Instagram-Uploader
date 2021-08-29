import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix=".", description="Soon")


@client.command()
async def loads(ctx, extension):
    client.load_extension(f"cogs.{extension}")


@client.command()
async def unloads(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run("ODc5MDg3NDEyODgwNDk4NzY4.YSKn8w.NZkNRPwhamy4WGBII9Y6e89E9vY")
