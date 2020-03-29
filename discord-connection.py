import os
import discord
from dotenv import load_dotenv
import random

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
my_guild = os.getenv('DISCORD_GUILD')
client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=my_guild)

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Saudações, jovem pupilo, {member.name}... Seja bem vindo'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content in ('Oi', 'Mestre', 'oi', 'saudações', 'mestre', 'Saudações'):
        await message.channel.send('Olá aventureiro, a cada ato de bravura, vocês crescerão mais e mais e serão recompensados a tempo.')

    if (message.content in ('1d100')):
        result = random.randint(0, 99)
        await message.channel.send("% d" % (result))
    
client.run(token)
