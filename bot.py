import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from discord.utils import find

@client.event
async def on_ready():
	print('ainsley')
	print('')
	print('Logged in as:')
	print(client.user.name)
	print('')
	print('Client User ID:')
	print(client.user.id)
	print('')
	await client.change_presence(game=discord.Game(name='meat' type=3))

Client = discord.Client()
client = commands.Bot(command_prefix = "s!")

@client.event
async def on_ready():
    print("Susan Bot is ready to demonetise!")

@client.event
async def on_message(message):

    if message.content.startswith("pls beg"):
        await client.send_message(message.channel,"pls beg")
        
    if message.content.upper().startswith("pls beg"):
    
        await client.send_message(message.channel,"pls beg")
        
    if message.content.upper().startswith("qolpak"):
    
        await client.send_message(message.channel,"qolpak")

    if message.content.upper().startswith("qolpak"):
    
        await client.send_message(message.channel,"qolpak")
        
client.run(os.environ["TOKEN_DISCORD"])
