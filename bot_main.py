import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from bot_script import hxhx

load_dotenv()
TOKEN = os.environ['bot_token']

client = commands.Bot(command_prefix = '?')

print('started\n')

@client.event
async def on_ready():
    print(f'{client.user} is here to police ur speech!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return 0
    if message.content.startswith('?safe'):
        print(message.content)
        new_msg = hxhx(message.content)
        print(new_msg)
        await message.channel.send(new_msg)
        print('done')

client.run(TOKEN)
