import discord
import asyncio
import time
import DonggukCafeteria
secs = time.time()
tm = time.localtime(secs)
hour = tm.tm_hour
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):

    if message.content.startswith('!상록원3층'):
        if hour >= 14:  # 오후 2시 이후에는 석식 메뉴를 보여줌
            await message.channel.send(DonggukCafeteria.sangrokwon3fdinner)
        else:
            await message.channel.send(DonggukCafeteria.sangrokwon3flunch)
    elif message.content.startswith('!상록원2층'):
        if hour >= 14:
            await message.channel.send(DonggukCafeteria.sangrokwon2fdinner)
        else:
            await message.channel.send(DonggukCafeteria.sangrokwon2flunch)
    elif message.content.startswith('!상록원1층'):
        await message.channel.send(DonggukCafeteria.sangrokwon1f)
    elif message.content.startswith('!그루터기'):
        if hour >= 14:
            await message.channel.send(DonggukCafeteria.grutergi_lunch)
        else:
            await message.channel.send(DonggukCafeteria.grutergi_dinner)
    elif message.content.startswith('!가든쿡'):
        await message.channel.send(DonggukCafeteria.gardencook)
    elif message.content.startswith('!누리터'):
        await message.channel.send(DonggukCafeteria.nuriter)
    elif message.content.startswith('!남산학사'):
        if hour >= 14:
            await message.channel.send(DonggukCafeteria.dormitory_dinner)
        else:
            await message.channel.send(DonggukCafeteria.dormitory_lunch)
    elif message.content.startswith('!동식명령어'):
        await message.channel.send('명령어 목록\n!상록원3층\n!상록원2층\n!상록원1층\n!그루터기\n!가든쿡\n!누리터\n!남산학사')

client.run('token')