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
        print(f'{url = }')
        if valid_insta_url == url[:26]:
            image_path = final_image(url)
            print(f'{image_path = }')
            await ctx.send(file=discord.File("./" + image_path))
            os.remove("./" + image_path)
        else:
            await ctx.reply("Bad URL")


def setup(client):
    client.add_cog(InstaBot(client))
