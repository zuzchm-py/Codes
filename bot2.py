import discord
from discord.ext import commands
import password_generator
import random
import os
print(os.listdir('memes'))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_member_join(member):
    channel_id = 1244726414356250634  # Replace with your desired channel ID
    channel = bot.get_channel(channel_id)
    await channel.send(f"{member.mention} Welcome to the server!")

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def bye(ctx):
    await ctx.send('\\U0001f642')

@bot.command()
async def generate_password(ctx, length: int = 8):
    await ctx.send(password_generator.gen_pass(length))

@bot.command()
async def photos_show(ctx):
    names = os.listdir('memes')
    randoms = random.choice(names)
    with open ('memes/' + randoms, 'rb') as f:
        image = discord.File(f)
        await ctx.send(file = image)

bot.run("YOUR_TOKEN")