import os
import discord

os.environ['TOKEN']

client = discord.Client()


# registering an event
@client.event
async def on_ready():
    print('we are live as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Vi_'):
        await message.channel.send('Praise Vi, All hail /BPG/')


client.run(os.getenv('TOKEN'))
