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

    if message.content.startswith('!상록원3층'):
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

    elif message.content.startswith('!상록원1층'):
        import DonggukCafeteria
        await message.channel.send('상록원 1층 메뉴입니다.\n'+DonggukCafeteria.parse_dgu_coop(17))

    elif message.content.startswith('!그루터기'):
        import DonggukCafeteria
        if hour >= 14:
            await message.channel.send('그루터기 석식 메뉴입니다.\n----- 그루터기 A코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
                26) + '\n----- 그루터기 B코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
                28) + '\n----- 그루터기 PAN -----\n' + DonggukCafeteria.parse_dgu_coop(
                29) + '\n----- 그루터기 NOODLE -----\n' + DonggukCafeteria.parse_dgu_coop(30))
        else:
            await message.channel.send('그루터기 석식 메뉴입니다.\n----- 그루터기 A코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
                25) + '\n----- 그루터기 B코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
                27) + '\n----- 그루터기 PAN -----\n' + DonggukCafeteria.parse_dgu_coop(
                29) + '\n----- 그루터기 NOODLE -----\n' + DonggukCafeteria.parse_dgu_coop(30))

    elif message.content.startswith('!가든쿡'):
        import DonggukCafeteria
        await message.channel.send('가든쿡 메뉴입니다.\n----- 가든쿡 샐러드코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
            32) + '\n----- 가든쿡 파스타코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
            33) + '\n----- 가든쿡 리조또코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
            34) + '\n----- 가든쿡 볶음밥코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
            35) + '\n----- 가든쿡 피자코너 -----\n' + DonggukCafeteria.parse_dgu_coop(36))

    elif message.content.startswith('!누리터'):
        import DonggukCafeteria
        await message.channel.send('누리터식당(일산) 메뉴입니다.\n----- 누리터 조식뷔페 -----\n' + DonggukCafeteria.parse_dgu_coop(
            40) + '\n----- 누리밥상 중식메뉴 -----\n' + DonggukCafeteria.parse_dgu_coop(
            41) + '\n----- 누리밥상 석식메뉴 -----\n' + DonggukCafeteria.parse_dgu_coop(
            42) + '\n----- 누리터 더진국 -----\n' + DonggukCafeteria.parse_dgu_coop(
            43) + '\n----- 누리터 팬앤누들 -----\n'+ DonggukCafeteria.parse_dgu_coop(44))

    elif message.content.startswith('!남산학사'):
        import DonggukCafeteria
        if hour >= 14:
            await message.channel.send('남산학사(기숙사)식당 석식 메뉴입니다.\n----- 남산학사 조식뷔페 -----\n' + DonggukCafeteria.parse_dgu_coop(
                46) + '\n----- 남산학사 A코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
                48) + '\n----- 남산학사 B코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
                50) + '\n----- 남산학사 푸드코트 -----\n' + DonggukCafeteria.parse_dgu_coop(51))
        else:
            await message.channel.send(
                '남산학사(기숙사)식당 중식 메뉴입니다.\n----- 남산학사 조식뷔페 -----\n' + DonggukCafeteria.parse_dgu_coop(
                    46) + '\n----- 남산학사 A코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
                    47) + '\n----- 남산학사 B코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
                    49) + '\n----- 남산학사 푸드코트 -----\n' + DonggukCafeteria.parse_dgu_coop(51))

    elif message.content.startswith('!동식명령어'):
        await message.channel.send('명령어 목록\n!상록원3층\n!상록원2층\n!상록원1층\n!그루터기\n!가든쿡\n!누리터\n!남산학사')

client.run('token')