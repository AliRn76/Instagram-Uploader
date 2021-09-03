import os
from discord.ext import commands

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

client.run("")
