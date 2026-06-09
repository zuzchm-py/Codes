import discord
from discord.ext import commands
import random
import requests
import os
import password_generator as bot_logic_password

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='$', intents=intents)

def get_fox_image_url():
    response = requests.get('https://randomfox.ca/floof/')
    data = response.json()
    return data['image']

@bot.command(name='fox')
async def fox(ctx):
    '''When the fox command is executed, the programme calls the get_fox_image_url function'''
    image_url = get_fox_image_url()
    await ctx.send(image_url)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel is not None:
        await channel.send(f"{member.mention} Welcome to the server!")

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def bye(ctx):
    await ctx.send('\\U0001f642')

@bot.command()
async def generate_password(ctx, length=8):
    await ctx.send(bot_logic_password.gen_pass(length))

@bot.command()
async def photos_show(ctx):
    names = os.listdir('animal_memes')
    randoms = random.choice(names)
    with open('animal_memes/' + randoms, 'rb') as f:
        image = discord.File(f, filename=randoms)
        await ctx.send(file=image)

@bot.command()
async def animals(ctx):
    names = os.listdir('animal_memes')
    randoms = random.choice(names)
    with open('animal_memes/' + randoms, 'rb') as f:
        image = discord.File(f, filename=randoms)
        await ctx.send(file=image)

bot.run("YOUR_TOKEN")
