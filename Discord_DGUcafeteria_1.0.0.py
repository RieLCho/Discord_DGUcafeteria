import discord
import asyncio
import time
import DonggukCafeteria

secs = time.time()
tm = time.localtime(secs)
hour = tm.tm_hour
client = discord.Client()

sangrokwon3flunch = discord.Embed(title="상록원 3층 중식메뉴", description="\n----- 상록원 집밥 -----\n" + DonggukCafeteria.parse_dgu_coop(
    2) + '\n----- 상록원 한그릇 -----\n' + DonggukCafeteria.parse_dgu_coop(
    4) + '\n----- 상록원 채식당 -----\n' + DonggukCafeteria.parse_dgu_coop(6), color=0x00ff00)

sangrokwon3fdinner = discord.Embed(title='상록원 3층 석식메뉴', description='\n----- 상록원 집밥 -----\n' + DonggukCafeteria.parse_dgu_coop(
    3) + '\n----- 상록원 한그릇 -----\n' + DonggukCafeteria.parse_dgu_coop(
    5) + '\n----- 상록원 채식당 -----\n' + DonggukCafeteria.parse_dgu_coop(6), color=0x00ff00)
sangrokwon2flunch = discord.Embed(title='상록원 2층 중식 메뉴', description='\n----- 상록원 백반코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
    8) + '\n----- 상록원 일품코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
    10) + '\n----- 상록원 양식코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
    12) + '\n----- 상록원 뚝배기코너 -----\n' + DonggukCafeteria.parse_dgu_coop(14), color=0x00ff00)
sangrokwon2fdinner = discord.Embed(title='상록원 2층 석식 메뉴', description='\n----- 상록원 백반코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
    9) + '\n----- 상록원 일품코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
    11) + '\n----- 상록원 양식코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
    13) + '\n----- 상록원 뚝배기코너 -----\n' + DonggukCafeteria.parse_dgu_coop(15), color=0x00ff00)
sangrokwon1f = discord.Embed(title='상록원 1층 메뉴', description=DonggukCafeteria.parse_dgu_coop(17), color=0x00ff00)
grutergi_lunch = discord.Embed(title='그루터기 중식 메뉴', description='\n----- 그루터기 A코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
    26) + '\n----- 그루터기 B코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
    28) + '\n----- 그루터기 PAN -----\n' + DonggukCafeteria.parse_dgu_coop(
    29) + '\n----- 그루터기 NOODLE -----\n' + DonggukCafeteria.parse_dgu_coop(30), color=0x00ff00)
grutergi_dinner = discord.Embed(title='그루터기 석식 메뉴', description='\n----- 그루터기 A코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
    25) + '\n----- 그루터기 B코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
    27) + '\n----- 그루터기 PAN -----\n' + DonggukCafeteria.parse_dgu_coop(
    29) + '\n----- 그루터기 NOODLE -----\n' + DonggukCafeteria.parse_dgu_coop(30), color=0x00ff00)
gardencook = discord.Embed(title='가든쿡 메뉴', description='\n----- 가든쿡 샐러드코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
    32) + '\n----- 가든쿡 파스타코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
    33) + '\n----- 가든쿡 리조또코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
    34) + '\n----- 가든쿡 볶음밥코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
    35) + '\n----- 가든쿡 피자코너 -----\n' + DonggukCafeteria.parse_dgu_coop(36), color=0x00ff00)
nuriter = discord.Embed(title='누리터식당(일산) 메뉴', description='\n----- 누리터 조식뷔페 -----\n' + DonggukCafeteria.parse_dgu_coop(
    40) + '\n----- 누리밥상 중식메뉴 -----\n' + DonggukCafeteria.parse_dgu_coop(
    41) + '\n----- 누리밥상 석식메뉴 -----\n' + DonggukCafeteria.parse_dgu_coop(
    42) + '\n----- 누리터 더진국 -----\n' + DonggukCafeteria.parse_dgu_coop(
    43) + '\n----- 누리터 팬앤누들 -----\n' + DonggukCafeteria.parse_dgu_coop(44), color=0x00ff00)
dormitory_lunch = discord.Embed(title='남산학사(기숙사)식당 중식 메뉴', description='\n----- 남산학사 조식뷔페 -----\n' + DonggukCafeteria.parse_dgu_coop(
    46) + '\n----- 남산학사 A코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
    47) + '\n----- 남산학사 B코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
    49) + '\n----- 남산학사 푸드코트 -----\n' + DonggukCafeteria.parse_dgu_coop(51), color=0x00ff00)
dormitory_dinner = discord.Embed(title='남산학사(기숙사)식당 석식 메뉴', description='\n----- 남산학사 조식뷔페 -----\n' + DonggukCafeteria.parse_dgu_coop(
    46) + '\n----- 남산학사 A코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
    48) + '\n----- 남산학사 B코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
    50) + '\n----- 남산학사 푸드코트 -----\n' + DonggukCafeteria.parse_dgu_coop(51), color=0x00ff00)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("!동식아 for help"))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):

    if message.content.startswith('!상록원3층'):
        if hour >= 14:  # 오후 2시 이후에는 석식 메뉴를 보여줌
            await message.channel.send(sangrokwon3fdinner)
        else:
            await message.channel.send(embed=sangrokwon3flunch)
    elif message.content.startswith('!석식상록원3층'):
        await message.channel.send(embed=sangrokwon3fdinner)
    elif message.content.startswith('!중식상록원3층'):
        await message.channel.send(embed=sangrokwon3flunch)

    elif message.content.startswith('!상록원2층'):
        if hour >= 14:
            await message.channel.send(embed=sangrokwon2fdinner)
        else:
            await message.channel.send(embed=sangrokwon2flunch)
    elif message.content.startswith('!석식상록원2층'):
        await message.channel.send(embed=sangrokwon2fdinner)
    elif message.content.startswith('!중식상록원2층'):
        await message.channel.send(embed=sangrokwon2flunch)
    elif message.content.startswith('!상록원1층'):
        await message.channel.send(embed=sangrokwon1f)

    elif message.content.startswith('!그루터기'):
        if hour >= 14:
            await message.channel.send(embed=grutergi_lunch)
        else:
            await message.channel.send(embed=grutergi_dinner)
    elif message.content.startswith('!석식그루터기'):
        await message.channel.send(embed=grutergi_lunch)
    elif message.content.startswith('!중식그루터기'):
        await message.channel.send(embed=grutergi_dinner)

    elif message.content.startswith('!가든쿡'):
        await message.channel.send(embed=gardencook)

    elif message.content.startswith('!누리터'):
        await message.channel.send(embed=nuriter)

    elif message.content.startswith('!남산학사'):
        if hour >= 14:
            await message.channel.send(embed=dormitory_dinner)
        else:
            await message.channel.send(embed=dormitory_lunch)
    elif message.content.startswith('!석식남산학사'):
        await message.channel.send(embed=dormitory_dinner)
    elif message.content.startswith('!중식남산학사'):
        await message.channel.send(embed=dormitory_lunch)

    elif message.content.startswith('!동식아'):
        embed = discord.Embed(title="동국대도 식후경 봇 명령어", description='!상록원3층\n!상록원2층\n!상록원1층\n!그루터기\n!가든쿡\n!누리터\n!남산학사', color=0x00ff00)
        await message.channel.send(embed=embed)
        await message.channel.send('자세한 설명은 !동식명령어 에서 확인하실 수 있습니다.')

    elif message.content.startswith('!동식명령어'):
        await message.channel.send('동국대도 식후경 봇 명령어\n!상록원3층\n!상록원2층\n!상록원1층\n!그루터기\n!가든쿡\n!누리터\n!남산학사\n!만든사람\n!중식0000 or !석식0000을 통해 중식혹은 석식을 확인할 수 있습니다. (기본적으로는 시간에 따라 알맞는 메뉴를 보여줍니다.) ex)!석식상록원3층')

    elif message.content.startswith('!만든사람'):
        developer_embed = discord.Embed(title='동식이 아빠', description='동국대학교 컴퓨터공학과 19학번 조양진\n버그문의는 깃헙 이슈 혹은 이메일로 부탁드려요!\nhttps://github.com/sheepjin99/Discord_DGUcafeteria\nEmail: 7033942cyj@dgu.ac.kr', color=0xff0000)
        await message.channel.send(embed=developer_embed)
        await message.channel.send('!엘프사이콩그루')

    elif message.content.startswith('!엘프사이콩그루'):
        diver_embed = discord.Embed(title="현재 세계선 다이버전스", description='1.130426%', color=0x0000ff)
        await message.channel.send(embed=diver_embed)
client.run('token')
