import asyncio, discord
import os, traceback, linecache, logging
import re, time, datetime
import textwrap
from discord.ext import commands
from discord.state import ConnectionState
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from utils import checks
from utils.funcs import Funcs

Client = discord.Client()
client = commands.Bot(command_prefix = "s!")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

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

client.run("NDMzODMyNzk3ODgzNDY1NzMx.DcfHAg.kKfBd5qOtkEjRU-v0qN4avcEJbQ")
