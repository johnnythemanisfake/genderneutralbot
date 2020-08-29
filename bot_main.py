import os
import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
from bot_script import hxhx

load_dotenv()
TOKEN = os.environ['bot_token']

client = commands.Bot(command_prefix = '?')

print('started\n')

async def stay_alive():
    print('smth')
    await asyncio.sleep(1500)

@client.event
async def on_ready():
    print(f'{client.user} is here to police ur speech!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return 0
    if message.content.startswith('?safe'):
        new_msg = hxhx(message.content)
        await message.channel.send(new_msg)

client.loop.create_task(stay_alive())
client.run(TOKEN)
