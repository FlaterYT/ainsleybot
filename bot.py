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
        
const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
    console.log('I am ready!');
});

client.on('message', message => {
    if (message.content === 'ping') {
    	message.reply('pong');
  	}
});

client.login(process.env.BOT_TOKEN);
