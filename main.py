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
    if message.content.startswith('!학식'):
        import DonggukCafeteria
        result = str(DonggukCafeteria.parse_dgu_coop(2))
        await message.channel.send(result)

    elif message.content.startswith('!say'):
        await message.channel.send('leave message')


client.run('Njg2NTgxNDY4OTAxODAyMDM1.XmptKA.sf5JPNkXImQRcu6BIGCDZGHstd0')