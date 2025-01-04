from ken import gen_pass
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def pass_gen(ctx, count_heh = 5):
    await ctx.send(gen_pass(count_heh)) 

@bot.command()
async def selamat_datang(ctx):
    await ctx.send("welcome")

@bot.command()
async def tolong(ctx):
    await ctx.send("apa ada yang bisa saya bantu?")

bot.run("Token")
