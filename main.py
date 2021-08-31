import os
import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
os.environ['TOKEN']
client = discord.Client()


# registering an event
@client.event
async def on_ready():
    print('we are live as {0.user}'.format(client))


@bot.command()
async def calc(ctx, arg):
    await ctx.send(arg)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!help'):
        await message.channel.send('`commands:\n!help: show this dialoge\n!dice: role a dice\n!calc: calculates your stuff`')

    if message.content.startswith('!dice'):
        rand_num = random.randint(1, 6)
        await message.channel.send('here is your lucky number: ' + str(rand_num) )


client.run(os.getenv('TOKEN'))
