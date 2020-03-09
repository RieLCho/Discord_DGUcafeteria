import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        await message.channel.send('test!!!!')

    elif message.content.startswith('!say'):
        await message.channel.send('leave message')


client.run('Njg2NTgxNDY4OTAxODAyMDM1.XmZU5w.mOfLEz8qJY-yfJpgCjSHxuGHB88')