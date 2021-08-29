import discord
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Activity(
            type=discord.ActivityType.listening, name="programming_n1 | prefix: .help"))
        print("Bot Online...")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('send me url...')


def setup(client):
    client.add_cog(Events(client))
