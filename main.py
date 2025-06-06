import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Big bot here {bot.user.name}')

@bot.event
async def on_member_join(member):
    await member.send("why are you here")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if "wordle" in message.content.lower():
        await message.channel.send("I love wordle too!")

    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
