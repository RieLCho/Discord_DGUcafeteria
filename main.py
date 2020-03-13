import discord
import asyncio
import time

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
    if message.content.startswith('!학식'):
        import DonggukCafeteria
        result = str(DonggukCafeteria.parse_dgu_coop(2))
        await message.channel.send(result)

    elif message.content.startswith('!상록원3층'):
        import DonggukCafeteria
        if hour >= 14:
            await message.channel.send('상록원 3층 석식 메뉴입니다.\n----- 상록원 집밥 -----\n' + DonggukCafeteria.parse_dgu_coop(
                3) + '\n----- 상록원 한그릇 -----\n' + DonggukCafeteria.parse_dgu_coop(
                5) + '\n----- 상록원 채식당 -----\n' + DonggukCafeteria.parse_dgu_coop(
                6))
        else:
            await message.channel.send('상록원 3층 중식 메뉴입니다.\n----- 상록원 집밥 -----\n'+DonggukCafeteria.parse_dgu_coop(
                2)+'\n----- 상록원 한그릇 -----\n'+DonggukCafeteria.parse_dgu_coop(
                4)+'\n----- 상록원 채식당 -----\n'+DonggukCafeteria.parse_dgu_coop(
                6))

    elif message.content.startswith('!상록원2층'):
        import DonggukCafeteria
        if hour >= 14:
            await message.channel.send('상록원 2층 석식 메뉴입니다.\n----- 상록원 백반코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
                9) + '\n----- 상록원 일품코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
                11) + '\n----- 상록원 양식코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
                13) + '\n----- 상록원 뚝배기코너 -----\n' + DonggukCafeteria.parse_dgu_coop(15))
        else:
            await message.channel.send('상록원 2층 중식 메뉴입니다.\n----- 상록원 백반코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
                8) + '\n----- 상록원 일품코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
                10) + '\n----- 상록원 양식코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
                12) + '\n----- 상록원 뚝배기코너 -----\n' + DonggukCafeteria.parse_dgu_coop(14))



client.run('token')