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
        
    while True:
        if heroku:
            token = os.environ['TOKEN']
        else:
            token = get_config_value('config', 'token')
        try:
            bot.run(token, bot=False)
        except discord.errors.LoginFailure:
            if not heroku:
                if _silent:
                    print('Cannot use setup Wizard becaue of silent mode')
                    exit(0)
                print("It seems the token you entered is incorrect or has changed. If you changed your password or enabled/disabled 2fa, your token will change. Grab your new token. Here's how you do it:\n")
                print("Go into your Discord window and press Ctrl+Shift+I (Ctrl+Opt+I can also work on macOS)")
                print("Then, go into the Applications tab (you may have to click the arrow at the top right to get there), expand the 'Local Storage' dropdown, select discordapp, and then grab the token value at the bottom. Here's how it looks: https://imgur.com/h3g9uf6")
                print("Paste the contents of that entry below.")
                print("-------------------------------------------------------------")
                token = input("| ").strip('"')
                with open("settings/config.json", "r+", encoding="utf8") as fp:
                    config = json.load(fp)
                    config["token"] = token
                    fp.seek(0)
                    fp.truncate()
                    json.dump(config, fp, indent=4)
                continue
        break
