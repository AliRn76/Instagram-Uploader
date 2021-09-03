import discord
from discord.ext import commands
import asyncio
import random
import uuid
import requests
import shutil

valid_images = ["png", "jpeg", "jpg"]


class InstaBot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="image")
    async def image(self, ctx):
        imageName = str(uuid.uuid4()) + '.jpg'
        await ctx.message.attachments[0].save("images/" + imageName)

    @commands.command(name="url")
    async def url(self, ctx, url):
        if url[0:26] == "https://cdn.discordapp.com" and url[-3:] in valid_images:
            r = requests.get(url, stream=True)
            imageName = str(uuid.uuid4()) + '.jpg'
            with open("images/" + imageName, 'wb') as out_file:
                print('Saving image: ' + imageName)
                shutil.copyfileobj(r.raw, out_file)


def setup(client):
    client.add_cog(InstaBot(client))
