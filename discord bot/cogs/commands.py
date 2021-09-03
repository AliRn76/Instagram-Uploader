import os
import uuid
import random
import shutil
import discord
import requests
from app import final_image
from discord.ext import commands


valid_images = ['png', 'jpeg', 'jpg']

def random_image() -> str:
    image_path = random.choice(os.listdir('../images/'))
    return image_path

class InstaBot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='image')
    async def image(self, ctx):
        image_name = str(uuid.uuid4()) + '.jpg'
        await ctx.message.attachments[0].save('images/' + image_name)

    @commands.command(name="url")
    async def url(self, ctx, url):
        if url[0:26] == 'https://cdn.discordapp.com' and url[-3:] in valid_images:
            r = requests.get(url, stream=True)
            image_name = str(uuid.uuid4()) + '.jpg'
            with open('images/' + image_name, 'wb') as out_file:
                print('Saving image: ' + image_name)
                shutil.copyfileobj(r.raw, out_file)

    @commands.command(name='watermark')
    async def watermark(self, ctx):
        new_path = final_image(random_image())
        await ctx.send(file=discord.File(new_path))


def setup(client):
    client.add_cog(InstaBot(client))
