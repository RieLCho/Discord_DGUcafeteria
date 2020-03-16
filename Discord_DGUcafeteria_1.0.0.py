# made by Yangjin Cho.

import time
import discord
import DonggukCafeteria
import logging

secs = time.time()
tm = time.localtime(secs)
hour = tm.tm_hour
client = discord.Client()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler("Discord_DGUcafeteria_1.0.0.py.log")
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


class MenuCollection:
    day = 0
    sangrokwon3flunch = discord.Embed(title="상록원 3층 중식메뉴", description="\n----- 상록원 집밥 -----\n" + DonggukCafeteria.parse_dgu_coop(
        2, day) + '\n----- 상록원 한그릇 -----\n' + DonggukCafeteria.parse_dgu_coop(
        4, day) + '\n----- 상록원 채식당 -----\n' + DonggukCafeteria.parse_dgu_coop(6, day), color=0x00ff00)

    sangrokwon3fdinner = discord.Embed(title='상록원 3층 석식메뉴', description='\n----- 상록원 집밥 -----\n' + DonggukCafeteria.parse_dgu_coop(
        3, day) + '\n----- 상록원 한그릇 -----\n' + DonggukCafeteria.parse_dgu_coop(
        5, day) + '\n----- 상록원 채식당 -----\n' + DonggukCafeteria.parse_dgu_coop(6, day), color=0x00ff00)
    sangrokwon2flunch = discord.Embed(title='상록원 2층 중식 메뉴', description='\n----- 상록원 백반코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
        8, day) + '\n----- 상록원 일품코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
        10, day) + '\n----- 상록원 양식코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
        12, day) + '\n----- 상록원 뚝배기코너 -----\n' + DonggukCafeteria.parse_dgu_coop(14, day), color=0x00ff00)
    sangrokwon2fdinner = discord.Embed(title='상록원 2층 석식 메뉴', description='\n----- 상록원 백반코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
        9, day) + '\n----- 상록원 일품코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
        11, day) + '\n----- 상록원 양식코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
        13, day) + '\n----- 상록원 뚝배기코너 -----\n' + DonggukCafeteria.parse_dgu_coop(15, day), color=0x00ff00)
    sangrokwon1f = discord.Embed(title='상록원 1층 메뉴', description=DonggukCafeteria.parse_dgu_coop(17, day), color=0x00ff00)
    grutergi_lunch = discord.Embed(title='그루터기 중식 메뉴', description='\n----- 그루터기 A코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
        26, day) + '\n----- 그루터기 B코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
        28, day) + '\n----- 그루터기 PAN -----\n' + DonggukCafeteria.parse_dgu_coop(
        29, day) + '\n----- 그루터기 NOODLE -----\n' + DonggukCafeteria.parse_dgu_coop(30, day), color=0x00ff00)
    grutergi_dinner = discord.Embed(title='그루터기 석식 메뉴', description='\n----- 그루터기 A코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
        25, day) + '\n----- 그루터기 B코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
        27, day) + '\n----- 그루터기 PAN -----\n' + DonggukCafeteria.parse_dgu_coop(
        29, day) + '\n----- 그루터기 NOODLE -----\n' + DonggukCafeteria.parse_dgu_coop(30, day), color=0x00ff00)
    gardencook = discord.Embed(title='가든쿡 메뉴', description='\n----- 가든쿡 샐러드코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
        32, day) + '\n----- 가든쿡 파스타코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
        33, day) + '\n----- 가든쿡 리조또코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
        34, day) + '\n----- 가든쿡 볶음밥코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
        35, day) + '\n----- 가든쿡 피자코너 -----\n' + DonggukCafeteria.parse_dgu_coop(36, day), color=0x00ff00)
    nuriter = discord.Embed(title='누리터식당(일산) 메뉴', description='\n----- 누리터 조식뷔페 -----\n' + DonggukCafeteria.parse_dgu_coop(
        40, day) + '\n----- 누리밥상 중식메뉴 -----\n' + DonggukCafeteria.parse_dgu_coop(
        41, day) + '\n----- 누리밥상 석식메뉴 -----\n' + DonggukCafeteria.parse_dgu_coop(
        42, day) + '\n----- 누리터 더진국 -----\n' + DonggukCafeteria.parse_dgu_coop(
        43, day) + '\n----- 누리터 팬앤누들 -----\n' + DonggukCafeteria.parse_dgu_coop(44, day), color=0x00ff00)
    dormitory_lunch = discord.Embed(title='남산학사(기숙사)식당 중식 메뉴', description='\n----- 남산학사 조식뷔페 -----\n' + DonggukCafeteria.parse_dgu_coop(
        46, day) + '\n----- 남산학사 A코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
        47, day) + '\n----- 남산학사 B코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
        49, day) + '\n----- 남산학사 푸드코트 -----\n' + DonggukCafeteria.parse_dgu_coop(51, day), color=0x00ff00)
    dormitory_dinner = discord.Embed(title='남산학사(기숙사)식당 석식 메뉴', description='\n----- 남산학사 조식뷔페 -----\n' + DonggukCafeteria.parse_dgu_coop(
        46, day) + '\n----- 남산학사 A코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
        48, day) + '\n----- 남산학사 B코너 -----\n' + DonggukCafeteria.parse_dgu_coop(
        50, day) + '\n----- 남산학사 푸드코트 -----\n' + DonggukCafeteria.parse_dgu_coop(51, day), color=0x00ff00)


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
            await message.channel.send(embed=MenuCollection.sangrokwon3fdinner)
            logger.info("Today's sangrokwon3fdinner sent")
        else:
            await message.channel.send(embed=MenuCollection.sangrokwon3flunch)
            logger.info("Today's sangrokwon3flunch sent")
    elif message.content.startswith('!석식상록원3층'):
        await message.channel.send(embed=MenuCollection.sangrokwon3fdinner)
        logger.info("Today's sangrokwon3fdinner sent")

    elif message.content.startswith('!중식상록원3층'):
        await message.channel.send(embed=MenuCollection.sangrokwon3flunch)
        logger.info("Today's sangrokwon3flunch sent")

    elif message.content.startswith('!상록원2층'):
        if hour >= 14:
            await message.channel.send(embed=MenuCollection.sangrokwon2fdinner)
            logger.info("Today's sangrokwon2fdinner sent")

        else:
            await message.channel.send(embed=MenuCollection.sangrokwon2flunch)
            logger.info("Today's sangrokwon2flunch sent")

    elif message.content.startswith('!석식상록원2층'):
        await message.channel.send(embed=MenuCollection.sangrokwon2fdinner)
        logger.info("Today's sangrokwon2fdinner sent")

    elif message.content.startswith('!중식상록원2층'):
        await message.channel.send(embed=MenuCollection.sangrokwon2flunch)
        logger.info("Today's sangrokwon2flunch sent")

    elif message.content.startswith('!상록원1층'):
        await message.channel.send(embed=MenuCollection.sangrokwon1f)
        logger.info("Today's sangrokwon1f sent")


    elif message.content.startswith('!그루터기'):
        if hour >= 14:
            await message.channel.send(embed=MenuCollection.grutergi_lunch)
            logger.info("Today's grutergi_lunch sent")

        else:
            await message.channel.send(embed=MenuCollection.grutergi_dinner)
            logger.info("Today's grutergi_dinner sent")

    elif message.content.startswith('!석식그루터기'):
        await message.channel.send(embed=MenuCollection.grutergi_lunch)
        logger.info("Today's grutergi_dinner sent")

    elif message.content.startswith('!중식그루터기'):
        await message.channel.send(embed=MenuCollection.grutergi_dinner)
        logger.info("Today's grutergi_lunch sent")


    elif message.content.startswith('!가든쿡'):
        await message.channel.send(embed=MenuCollection.gardencook)
        logger.info("Today's gardencook sent")


    elif message.content.startswith('!누리터'):
        await message.channel.send(embed=MenuCollection.nuriter)
        logger.info("Today's nuriter sent")


    elif message.content.startswith('!남산학사'):
        if hour >= 14:
            await message.channel.send(embed=MenuCollection.dormitory_dinner)
            logger.info("Today's dormitory_dinner sent")

        else:
            await message.channel.send(embed=MenuCollection.dormitory_lunch)
            logger.info("Today's dormitory_lunch sent")

    elif message.content.startswith('!석식남산학사'):
        await message.channel.send(embed=MenuCollection.dormitory_dinner)
        logger.info("Today's dormitory_dinner sent")

    elif message.content.startswith('!중식남산학사'):
        await message.channel.send(embed=MenuCollection.dormitory_lunch)
        logger.info("Today's dormitory_lunch sent")

    elif message.content.startswith('!동식아'):
        embed = discord.Embed(title="동국대도 식후경 봇 명령어", description='!상록원3층\n!상록원2층\n!상록원1층\n!그루터기\n!가든쿡\n!누리터\n!남산학사', color=0x00ff00)
        await message.channel.send(embed=embed)
        await message.channel.send('자세한 설명은 !동식명령어 에서 확인하실 수 있습니다.')
        logger.info("help requested")


    elif message.content.startswith('!동식명령어'):
        await message.channel.send('동국대도 식후경 봇 명령어\n!상록원3층\n!상록원2층\n!상록원1층\n!그루터기\n!가든쿡\n!누리터\n!남산학사\n!만든사람\n!중식0000 or !석식0000을 통해 중식혹은 석식을 확인할 수 있습니다. (기본적으로는 시간에 따라 알맞는 메뉴를 보여줍니다.) ex)!석식상록원3층')
        logger.info("detailed help requested")

    elif message.content.startswith('!만든사람'):
        developer_embed = discord.Embed(title='동식이 아빠', description='동국대학교 컴퓨터공학과 19학번 조양진\n버그문의는 깃헙 이슈 혹은 이메일로 부탁드려요!\nhttps://github.com/sheepjin99/Discord_DGUcafeteria\nEmail: 7033942cyj@dgu.ac.kr', color=0xff0000)
        await message.channel.send(embed=developer_embed)
        await message.channel.send('!엘프사이콩그루')
        logger.info("credit requested")

    elif message.content.startswith('!엘프사이콩그루'):
        diver_embed = discord.Embed(title="현재 세계선 다이버전스", description='1.130426%', color=0x0000ff)
        await message.channel.send(embed=diver_embed)

    # elif message.content.startswith('!내일식단'):
    #     embed_tomorrow = discord.Embed(title="내일 식단을 가져옵니다.", description='명령어를 입력해주세요.', color=0x0000ff)
    #     await message.channel.send(embed=embed_tomorrow)
    #
    #     def check(m):
    #         return m.content == '!상록원3층'
    #     msg = await client.wait_for('message', check=check)
    #     if msg is None:
    #         MenuCollection.day -= 1
    #         embed_error = discord.Embed(title='15초로 내로 입력해주세요.', description='다시시도: !내일식단', color=0xff0000)
    #         await message.channel.send(embed=embed_error)
    #         logger.info("error")
    #     MenuCollection.day = 1
    #     if hour >= 14:  # 오후 2시 이후에는 석식 메뉴를 보여줌
    #         await message.channel.send(embed=MenuCollection.sangrokwon3fdinner)
    #         logger.info("Tomorrow's sangrokwon3fdinner sent")
    #     else:
    #         await message.channel.send(embed=MenuCollection.sangrokwon3flunch)
    #         logger.info("Tomorrow's sangrokwon3flunch sent")
    #
    #
    #     elif message.content.startswith('!상록원3층'):
    #         if hour >= 14:  # 오후 2시 이후에는 석식 메뉴를 보여줌
    #             await message.channel.send(embed=MenuCollection.sangrokwon3fdinner)
    #             logger.info("Tomorrow's sangrokwon3fdinner sent")
    #         else:
    #             await message.channel.send(embed=MenuCollection.sangrokwon3flunch)
    #             logger.info("Tomorrow's sangrokwon3flunch sent")
    #     elif message.content.startswith('!석식상록원3층'):
    #         await message.channel.send(embed=MenuCollection.sangrokwon3fdinner)
    #         logger.info("Tomorrow's sangrokwon3fdinner sent")
    #
    #     elif message.content.startswith('!중식상록원3층'):
    #         await message.channel.send(embed=MenuCollection.sangrokwon3flunch)
    #         logger.info("Tomorrow's sangrokwon3flunch sent")
    #
    #     elif message.content.startswith('!상록원2층'):
    #         if hour >= 14:
    #             await message.channel.send(embed=MenuCollection.sangrokwon2fdinner)
    #             logger.info("Tomorrow's sangrokwon2fdinner sent")
    #
    #         else:
    #             await message.channel.send(embed=MenuCollection.sangrokwon2flunch)
    #             logger.info("Tomorrow's sangrokwon2flunch sent")
    #
    #     elif message.content.startswith('!석식상록원2층'):
    #         await message.channel.send(embed=MenuCollection.sangrokwon2fdinner)
    #         logger.info("Tomorrow's sangrokwon2fdinner sent")
    #
    #     elif message.content.startswith('!중식상록원2층'):
    #         await message.channel.send(embed=MenuCollection.sangrokwon2flunch)
    #         logger.info("Tomorrow's sangrokwon2flunch sent")
    #
    #     elif message.content.startswith('!상록원1층'):
    #         await message.channel.send(embed=MenuCollection.sangrokwon1f)
    #         logger.info("Tomorrow's sangrokwon1f sent")
    #
    #     elif message.content.startswith('!그루터기'):
    #         if hour >= 14:
    #             await message.channel.send(embed=MenuCollection.grutergi_lunch)
    #             logger.info("Tomorrow's grutergi_lunch sent")
    #
    #         else:
    #             await message.channel.send(embed=MenuCollection.grutergi_dinner)
    #             logger.info("Tomorrow's grutergi_dinner sent")
    #
    #     elif message.content.startswith('!석식그루터기'):
    #         await message.channel.send(embed=MenuCollection.grutergi_lunch)
    #         logger.info("Tomorrow's grutergi_dinner sent")
    #
    #     elif message.content.startswith('!중식그루터기'):
    #         await message.channel.send(embed=MenuCollection.grutergi_dinner)
    #         logger.info("Tomorrow's grutergi_lunch sent")
    #
    #
    #     elif message.content.startswith('!가든쿡'):
    #         await message.channel.send(embed=MenuCollection.gardencook)
    #         logger.info("Tomorrow's gardencook sent")
    #
    #
    #     elif message.content.startswith('!누리터'):
    #         await message.channel.send(embed=MenuCollection.nuriter)
    #         logger.info("Tomorrow's nuriter sent")
    #
    #
    #     elif message.content.startswith('!남산학사'):
    #         if hour >= 14:
    #             await message.channel.send(embed=MenuCollection.dormitory_dinner)
    #             logger.info("Tomorrow's dormitory_dinner sent")
    #
    #         else:
    #             await message.channel.send(embed=MenuCollection.dormitory_lunch)
    #             logger.info("Tomorrow's dormitory_lunch sent")
    #
    #     elif message.content.startswith('!석식남산학사'):
    #         await message.channel.send(embed=MenuCollection.dormitory_dinner)
    #         logger.info("Tomorrow's dormitory_dinner sent")
    #
    #     elif message.content.startswith('!중식남산학사'):
    #         await message.channel.send(embed=MenuCollection.dormitory_lunch)
    #         logger.info("Tomorrow's dormitory_lunch sent")
    #
    #     else:
    #         MenuCollection.day -= 1
    #         embed_error = discord.Embed(title='잘못된 명령어입니다.', description='다시시도: !내일식단', color=0xff0000)
    #         await message.channel.send(embed=embed_error)
    #         logger.info("input error")

client.run('token')
