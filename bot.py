import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from discord.utils import find

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
        
@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("-------")
    serversConnected = str(len(client.guilds))
    print("Guilds connected: " + serversConnected)#Returns number of guilds connected to
    game=discord.Game(name='on ' + serversConnected + ' servers!')
    await client.change_presence(activity=game)
    try:
        await botlist.post_server_count(serversConnected, shardCount)
        print("Successfully published server count to dbl.")
    except Exception as e:
        print("Failed to post server count to tbl.")

while True:
    client.run(token) #runs the bot.
