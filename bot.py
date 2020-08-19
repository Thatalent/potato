import os

import discord
from discord.ext import commands
import random
import time
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'))

@bot.event
async def on_ready():
    print(f'Good day my spudly subjects! {bot.user} has descended on your roots!')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Greetings {member.name}, welcome to the Spuds Army! (gravy baths included)'
    )

@bot.command(name='spud_joke', help='responds with a two line potato joke. very punny')
async def spud_joke(ctx):
    spud_jokes = [
        ['What do you call a mean potato?',
        'A dictator'],
        ['What do you call a golden retriever that tosses around potatoes?',
        'Air Spud'],
        ['What do you can a potato smoking weed?',
        'Deep fried'],
        ['Hey spuddling, guess my favorite beer?',
        'Spudweiser'],
        ['What do you call a potato in an Iron Man suit?',
        'Tony Starch']
    ]
    response = random.choice(spud_jokes)
    await ctx.send(response[0])
    time.sleep(5)
    await ctx.send(response[1])

# @bot.command(name='')
    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if  message.content.startswith('!'):
        await bot.process_commands(message)
        return
    tato_list = ['spud', 'potato', 'root', 'overlord', 'spudpreme', 'supreme']
    if any(spud.upper() in message.content.upper() for spud in tato_list):
        spud_jokes = [
            ('I see you\'re flexing your spudliness.\n'
            'I approve'),
            ('Blue potato is a variety of potato that originates from South America. Skin and flesh of this potato are purple, but they become blue after cooking. Blue color comes from high concentration of pigment called anthocyanin.\n'
             '(Plants < Potato)'),
            ('This reminds me of when I first rose to my spudpreme power.\n'
            'It took abandoning my roots and toppling soil!'),
            'You\'ll one russet potato some day.',
            'Your comment was appealing'
        ]
        response = random.choice(spud_jokes)
        await message.channel.send(response)
    if 'What do you call a mean potato' in message.content:
        await message.reply('a dictator')
    await bot.process_commands(message)



bot.run(TOKEN)