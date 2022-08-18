import discord
import os
import ipdb
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv("TOKEN")

# intents = discord.Intents.default()
# intents.members = True
# 
# bot = commands.Bot(intents=intents, command_prefix='!')
# 
# @bot.command()
# async def foo(ctx):
#     await ctx.channel.send("bar")
# 
# @bot.command()
# async def hello(ctx):
#     await ctx.channel.send("Hi there, {0.name}".format(ctx.author))
# 
# @bot.command()
# async def sayhi(ctx, arg):
#     found = None
#     for member in ctx.guild.members:
#         if member.name == arg:
#             found = member
# 
#     if found:
#         await ctx.message.channel.send(f"<@{found.id}> {ctx.message.author.name} says hello there!")
#     else:
#         await ctx.message.channel.send("I don't know who that is...")
# 
# @bot.command()
# async def ping(ctx):
#     await ctx.message.channel.send("Pong :sunglasses:")
# 
# bot.run(TOKEN)

class Meta(commands.Cog):
    def __init__(self):
        pass

class Winterbot(commands.Bot):
    def __init__(self):
        super().__init__(
                command_prefix = '!',
                intents = discord.Intents.default(),
                status = discord.Status.online,
                activity = discord.Game(name = "!help for information")
                )
        self.token = TOKEN

    @commands.command()
    async def hello(ctx):
        await ctx.channel.send("Hi there, {0.name}".format(ctx.author))

    @commands.command()
    async def sayhi(ctx, arg):
        found = None
        for member in ctx.guild.members:
            if member.name == arg:
                found = member

        if found:
            await ctx.message.channel.send(f"<@{found.id}> {ctx.message.author.name} says hello there!")
        else:
            await ctx.message.channel.send("I don't know who that is...")
    @commands.command()
    async def ping(ctx):
        await ctx.message.channel.send("Pong :sunglasses:")


    def run(self):
        super().run(TOKEN)


wb = Winterbot()
ipdb.set_trace()
