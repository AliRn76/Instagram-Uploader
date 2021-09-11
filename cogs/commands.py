import discord
import os
from discord.ext import commands
from app import final_image

valid_insta_url = "https://www.instagram.com/"

class InstaBot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='url')
    async def url(self, ctx, url):
        if valid_insta_url == url[:26]:
            image_path = final_image(url)
            await ctx.send(file=discord.File("/home/mahanbi/PYTHON/Instagram-Uploader/" + image_path))
            os.remove("/home/mahanbi/PYTHON/Instagram-Uploader/" + image_path)
        else:
            await ctx.reply("Bad URL")


def setup(client):
    client.add_cog(InstaBot(client))
