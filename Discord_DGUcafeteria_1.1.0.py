# made by Yangjin Cho.
# Check for latest release at https://github.com/sheepjin99/DonggukCafeteria/releases.

import random
import time
import discord
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
import logging

d = datetime.datetime.now()
d = d.replace(minute=00, hour=00, second=00)
d = (int(time.mktime(d.timetuple())))  # one day = 86400
posix = "&sday="+str(d)

secs = time.time()
tm = time.localtime(secs)
hour = tm.tm_hour
client = discord.Client()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler("MobileDonggukCafeteria.py.log")
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

html = urlopen("http://dgucoop.dongguk.edu/mobile/menu.html?code=5"+posix)
logger.info("DGUcoop Website Opened")
sang3f_source = html.read()
html.close()

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=7'+posix)
logger.info("DGUcoop Website Opened")
sang1f_source = html.read()
html.close()

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=1'+posix)
logger.info("DGUcoop Website Opened")
sang2f_source = html.read()
html.close()

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=2'+posix)
logger.info("DGUcoop Website Opened")
grutergi_source = html.read()
html.close()

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=0'+posix)
logger.info("DGUcoop Website Opened")
pan_noodle_source = html.read()
html.close()

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=9'+posix)
logger.info("DGUcoop Website Opened")
gardencook_source = html.read()
html.close()

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=8'+posix)
logger.info("DGUcoop Website Opened")
dorm_source = html.read()
html.close()

##############################################################################
d += 86400
posix = "&sday="+str(d)

html = urlopen("http://dgucoop.dongguk.edu/mobile/menu.html?code=5"+posix)
logger.info("DGUcoop Website Opened")
tomorrow_sang3f_source = html.read()
html.close()

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=7'+posix)
logger.info("DGUcoop Website Opened")
tomorrow_sang1f_source = html.read()
html.close()

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=1'+posix)
logger.info("DGUcoop Website Opened")
tomorrow_sang2f_source = html.read()
html.close()

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=2'+posix)
logger.info("DGUcoop Website Opened")
tomorrow_grutergi_source = html.read()
html.close()

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=0'+posix)
logger.info("DGUcoop Website Opened")
tomorrow_pan_noodle_source = html.read()
html.close()

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=9'+posix)
logger.info("DGUcoop Website Opened")
tomorrow_gardencook_source = html.read()
html.close()

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=8'+posix)
logger.info("DGUcoop Website Opened")
tomorrow_dorm_source = html.read()
html.close()

def sangrok_3f(tr, td, day=0):
    if day is 0:
        tasty_soup = BeautifulSoup(sang3f_source, "lxml")
    else:
        tasty_soup = BeautifulSoup(tomorrow_sang3f_source, "lxml")
    table = tasty_soup.find("table")
    tables = table
    menu_table = tables  # second table is the menu table what we are looking for
    menu_tr = menu_table.find_all('tr')  # tr number will be index of cafeteria
    cafeteria = menu_tr[tr]
    for span in tasty_soup.find_all("span"):
        span.replace_with("\n")
    menu_td = cafeteria.find_all('td')
    result = str(menu_td[td].text)
    if result is "":
        result = "데이터가 없습니다."
    return result


def sangrok_2f(tr, td, day=0):
    if day is 0:
        tasty_soup = BeautifulSoup(sang2f_source, "lxml")
    else:
        tasty_soup = BeautifulSoup(tomorrow_sang2f_source, "lxml")
    table = tasty_soup.find("table")
    tables = table
    menu_table = tables  # second table is the menu table what we are looking for
    menu_tr = menu_table.find_all('tr')  # tr number will be index of cafeteria
    cafeteria = menu_tr[tr]
    for span in tasty_soup.find_all("span"):
        span.replace_with("\n")
    menu_td = cafeteria.find_all('td')
    result = str(menu_td[td].text)
    if result is "":
        result = "데이터가 없습니다."
    return result



def sangrok_1f(tr=1, td=1, day=0):
    if day is 0:
        tasty_soup = BeautifulSoup(sang1f_source, "lxml")
    else:
        tasty_soup = BeautifulSoup(tomorrow_sang1f_source, "lxml")
    table = tasty_soup.find("table")
    tables = table
    menu_table = tables  # second table is the menu table what we are looking for
    menu_tr = menu_table.find_all('tr')  # tr number will be index of cafeteria
    cafeteria = menu_tr[tr]
    for span in tasty_soup.find_all("span"):
        span.replace_with("\n")
    menu_td = cafeteria.find_all('td')
    result = str(menu_td[td].text)
    if result is "":
        result = "데이터가 없습니다."
    return result

def grutergi(tr, td, day=0):
    if day is 0:
        tasty_soup = BeautifulSoup(grutergi_source, "lxml")
    else:
        tasty_soup = BeautifulSoup(tomorrow_grutergi_source, "lxml")
    table = tasty_soup.find("table")
    tables = table
    menu_table = tables  # second table is the menu table what we are looking for
    menu_tr = menu_table.find_all('tr')  # tr number will be index of cafeteria
    cafeteria = menu_tr[tr]
    for span in tasty_soup.find_all("span"):
        span.replace_with("\n")
    menu_td = cafeteria.find_all('td')
    result = str(menu_td[td].text)
    if result is "":
        result = "데이터가 없습니다."
    return result


def grutergi_pan_noodle(tr, td, day=0):
    if day is 0:
        tasty_soup = BeautifulSoup(pan_noodle_source, "lxml")
    else:
        tasty_soup = BeautifulSoup(tomorrow_pan_noodle_source, "lxml")
    table = tasty_soup.find("table")
    tables = table
    menu_table = tables  # second table is the menu table what we are looking for
    menu_tr = menu_table.find_all('tr')  # tr number will be index of cafeteria
    cafeteria = menu_tr[tr]
    for span in tasty_soup.find_all("span"):
        span.replace_with("\n")
    menu_td = cafeteria.find_all('td')
    result = str(menu_td[td].text)
    if result is "":
        result = "데이터가 없습니다."
    return result


def gardencook(tr, td, day=0):
    if day is 0:
        tasty_soup = BeautifulSoup(gardencook_source, "lxml")
    else:
        tasty_soup = BeautifulSoup(tomorrow_gardencook_source, "lxml")
    table = tasty_soup.find("table")
    tables = table
    menu_table = tables  # second table is the menu table what we are looking for
    menu_tr = menu_table.find_all('tr')  # tr number will be index of cafeteria
    cafeteria = menu_tr[tr]
    for span in tasty_soup.find_all("span"):
        span.replace_with("\n")
    menu_td = cafeteria.find_all('td')
    result = str(menu_td[td].text)
    if result is "":
        result = "데이터가 없습니다."
    return result

def dormitory(tr, td,day=0):
    if day is 0:
        tasty_soup = BeautifulSoup(dorm_source, "lxml")
    else:
        tasty_soup = BeautifulSoup(tomorrow_dorm_source, "lxml")
    table = tasty_soup.find("table")
    tables = table
    menu_table = tables  # second table is the menu table what we are looking for
    menu_tr = menu_table.find_all('tr')  # tr number will be index of cafeteria
    cafeteria = menu_tr[tr]
    for span in tasty_soup.find_all("span"):
        span.replace_with("\n")
    menu_td = cafeteria.find_all('td')
    result = str(menu_td[td].text)
    if result is "":
        result = "데이터가 없습니다."
    return result

sangrok_3f_jipbab_lunch = sangrok_3f(1,1)
sangrok_3f_jipbab_dinner = sangrok_3f(1,2)
sangrok_3f_hangurut_lunch = sangrok_3f(2,1)
sangrok_3f_hangurut_dinner = sangrok_3f(2,2)
sangrok_3f_vegeterian = sangrok_3f(3,1)

sangrok_2f_bakban_lunch = sangrok_2f(1,1)
sangrok_2f_bakban_dinner = sangrok_2f(1,2)
sangrok_2f_ilpum_lunch = sangrok_2f(2,1)
sangrok_2f_ilpum_dinner = sangrok_2f(2,2)
sangrok_2f_western_lunch = sangrok_2f(3,1)
sangrok_2f_western_dinner = sangrok_2f(3,2)
sangrok_2f_ttukbaegi_lunch = sangrok_2f(4,1)
sangrok_2f_ttukbaegi_dinner = sangrok_2f(4,2)

sangrok_1f_menu = sangrok_1f()

grutergi_A_lunch = grutergi(1,1)
grutergi_A_dinner = grutergi(1,2)
grutergi_B_lunch = grutergi(2,1)
grutergi_B_dinner = grutergi(2,2)

grutergi_pan_lunch = grutergi_pan_noodle(1,1)
grutergi_pan_dinner = grutergi_pan_noodle(1,2)
grutergi_noodle_lunch = grutergi_pan_noodle(2,1)
grutergi_noodle_dinner = grutergi_pan_noodle(2,2)


gardencook_salad = gardencook(1, 1)
gardencook_pasta = gardencook(2, 1)
gardencook_risotto = gardencook(3, 1)
gardencook_fried_rice = gardencook(4, 1)
gardencook_pizza = gardencook(5, 1)

dormitory_buffet_breakfast = dormitory(1,1)
dormitory_a_lunch = dormitory(2,2)
dormitory_a_dinner = dormitory(2,3)
dormitory_b_lunch = dormitory(3,2)
dormitory_b_dinner = dormitory(3,3)
dormitory_foodcourt_lunch = dormitory(4,2)
dormitory_foodcourt_dinner = dormitory(4,3)

###############################################################################

tomorrow_sangrok_3f_jipbab_lunch = sangrok_3f(1,1,1)
tomorrow_sangrok_3f_jipbab_dinner = sangrok_3f(1,2,1)
tomorrow_sangrok_3f_hangurut_lunch = sangrok_3f(2,1,1)
tomorrow_sangrok_3f_hangurut_dinner = sangrok_3f(2,2,1)
tomorrow_sangrok_3f_vegeterian = sangrok_3f(3,1,1)

tomorrow_sangrok_2f_bakban_lunch = sangrok_2f(1,1,1)
tomorrow_sangrok_2f_bakban_dinner = sangrok_2f(1,2,1)
tomorrow_sangrok_2f_ilpum_lunch = sangrok_2f(2,1,1)
tomorrow_sangrok_2f_ilpum_dinner = sangrok_2f(2,2,1)
tomorrow_sangrok_2f_western_lunch = sangrok_2f(3,1,1)
tomorrow_sangrok_2f_western_dinner = sangrok_2f(3,2,1)
tomorrow_sangrok_2f_ttukbaegi_lunch = sangrok_2f(4,1,1)
tomorrow_sangrok_2f_ttukbaegi_dinner = sangrok_2f(4,2,1)

tomorrow_sangrok_1f_menu = sangrok_1f()

tomorrow_grutergi_A_lunch = grutergi(1,1,1)
tomorrow_grutergi_A_dinner = grutergi(1,2,1)
tomorrow_grutergi_B_lunch = grutergi(2,1,1)
tomorrow_grutergi_B_dinner = grutergi(2,2,1)

tomorrow_grutergi_pan_lunch = grutergi_pan_noodle(1,1,1)
tomorrow_grutergi_pan_dinner = grutergi_pan_noodle(1,2,1)
tomorrow_grutergi_noodle_lunch = grutergi_pan_noodle(2,1,1)
tomorrow_grutergi_noodle_dinner = grutergi_pan_noodle(2,2,1)


tomorrow_gardencook_salad = gardencook(1, 1,1)
tomorrow_gardencook_pasta = gardencook(2, 1,1)
tomorrow_gardencook_risotto = gardencook(3, 1,1)
tomorrow_gardencook_fried_rice = gardencook(4, 1,1)
tomorrow_gardencook_pizza = gardencook(5, 1,1)

tomorrow_dormitory_buffet_breakfast = dormitory(1,1,1)
tomorrow_dormitory_a_lunch = dormitory(2,2,1)
tomorrow_dormitory_a_dinner = dormitory(2,3,1)
tomorrow_dormitory_b_lunch = dormitory(3,2,1)
tomorrow_dormitory_b_dinner = dormitory(3,3,1)
tomorrow_dormitory_foodcourt_lunch = dormitory(4,2,1)
tomorrow_dormitory_foodcourt_dinner = dormitory(4,3,1)

class MenuCollection:
    sangrokwon3flunch = discord.Embed(title="상록원 3층 중식메뉴", description="\n----- 상록원 집밥 -----\n" + sangrok_3f_jipbab_lunch + '\n----- 상록원 한그릇 -----\n' + sangrok_3f_hangurut_lunch + '\n----- 상록원 채식당 -----\n' + sangrok_3f_vegeterian, color=0x00ff00)
    sangrokwon3fdinner = discord.Embed(title='상록원 3층 석식메뉴', description='\n----- 상록원 집밥 -----\n' + sangrok_3f_jipbab_dinner + '\n----- 상록원 한그릇 -----\n' + sangrok_3f_hangurut_dinner + '\n----- 상록원 채식당 -----\n' + sangrok_3f_vegeterian, color=0x00ff00)
    sangrokwon2flunch = discord.Embed(title='상록원 2층 중식 메뉴', description='\n----- 상록원 백반코너 -----\n' + sangrok_2f_bakban_lunch + '\n----- 상록원 일품코너 -----\n' + sangrok_2f_ilpum_lunch + '\n----- 상록원 양식코너 -----\n' + sangrok_2f_western_lunch + '\n----- 상록원 뚝배기코너 -----\n' + sangrok_2f_ttukbaegi_lunch, color=0x00ff00)
    sangrokwon2fdinner = discord.Embed(title='상록원 2층 석식 메뉴', description='\n----- 상록원 백반코너 -----\n' + sangrok_2f_bakban_dinner + '\n----- 상록원 일품코너 -----\n' + sangrok_2f_ilpum_dinner + '\n----- 상록원 양식코너 -----\n' + sangrok_2f_western_dinner + '\n----- 상록원 뚝배기코너 -----\n' + sangrok_2f_ttukbaegi_dinner, color=0x00ff00)
    sangrokwon1f = discord.Embed(title='상록원 1층 메뉴', description=sangrok_1f_menu, color=0x00ff00)
    grutergi_lunch = discord.Embed(title='그루터기 중식 메뉴', description='\n----- 그루터기 A코너 -----\n' + grutergi_A_lunch + '\n----- 그루터기 B코너 -----\n' + grutergi_B_lunch + '\n----- 그루터기 PAN -----\n' + grutergi_pan_lunch + '\n----- 그루터기 NOODLE -----\n' + grutergi_noodle_lunch, color=0x00ff00)
    grutergi_dinner = discord.Embed(title='그루터기 석식 메뉴', description='\n----- 그루터기 A코너 -----\n' + grutergi_A_dinner + '\n----- 그루터기 B코너 -----\n' + grutergi_B_dinner + '\n----- 그루터기 PAN -----\n' + grutergi_pan_dinner + '\n----- 그루터기 NOODLE -----\n' + grutergi_noodle_dinner, color=0x00ff00)
    gardencook = discord.Embed(title='가든쿡 메뉴', description='\n----- 가든쿡 샐러드코너 -----\n' + gardencook_salad + '\n----- 가든쿡 파스타코너 -----\n' + gardencook_pasta + '\n----- 가든쿡 리조또코너 -----\n' + gardencook_risotto + '\n----- 가든쿡 볶음밥코너 -----\n' + gardencook_fried_rice + '\n----- 가든쿡 피자코너 -----\n' + gardencook_pizza, color=0x00ff00)
    dormitory_lunch = discord.Embed(title='남산학사(기숙사)식당 중식 메뉴', description='\n----- 남산학사 조식뷔페 -----\n' + dormitory_buffet_breakfast + '\n----- 남산학사 A코너 -----\n' + dormitory_a_lunch + '\n----- 남산학사 B코너 -----\n' + dormitory_b_lunch + '\n----- 남산학사 푸드코트 -----\n' + dormitory_foodcourt_lunch, color=0x00ff00)
    dormitory_dinner = discord.Embed(title='남산학사(기숙사)식당 석식 메뉴', description='\n----- 남산학사 조식뷔페 -----\n' + dormitory_buffet_breakfast + '\n----- 남산학사 A코너 -----\n' + dormitory_a_dinner + '\n----- 남산학사 B코너 -----\n' + dormitory_b_dinner + '\n----- 남산학사 푸드코트 -----\n' + dormitory_foodcourt_dinner, color=0x00ff00)
    # nuriter = discord.Embed(title='누리터식당(일산) 메뉴', description='\n----- 누리터 조식뷔페 -----\n' + DonggukCafeteria.parse_dgu_coop(40, day) + '\n----- 누리밥상 중식메뉴 -----\n' + DonggukCafeteria.parse_dgu_coop(41, day) + '\n----- 누리밥상 석식메뉴 -----\n' + DonggukCafeteria.parse_dgu_coop(42, day) + '\n----- 누리터 더진국 -----\n' + DonggukCafeteria.parse_dgu_coop(43, day) + '\n----- 누리터 팬앤누들 -----\n' + DonggukCafeteria.parse_dgu_coop(44, day), color=0x00ff00)

    tomorrow_sangrokwon3flunch = discord.Embed(title="내일 상록원 3층 중식메뉴", description="\n----- 상록원 집밥 -----\n" + tomorrow_sangrok_3f_jipbab_lunch + '\n----- 상록원 한그릇 -----\n' + tomorrow_sangrok_3f_hangurut_lunch + '\n----- 상록원 채식당 -----\n' + tomorrow_sangrok_3f_vegeterian, color=0x00ff00)
    tomorrow_sangrokwon3fdinner = discord.Embed(title='내일 상록원 3층 석식메뉴', description='\n----- 상록원 집밥 -----\n' + tomorrow_sangrok_3f_jipbab_dinner + '\n----- 상록원 한그릇 -----\n' + tomorrow_sangrok_3f_hangurut_dinner + '\n----- 상록원 채식당 -----\n' + tomorrow_sangrok_3f_vegeterian, color=0x00ff00)
    tomorrow_sangrokwon2flunch = discord.Embed(title='내일 상록원 2층 중식 메뉴', description='\n----- 상록원 백반코너 -----\n' + tomorrow_sangrok_2f_bakban_lunch + '\n----- 상록원 일품코너 -----\n' + tomorrow_sangrok_2f_ilpum_lunch + '\n----- 상록원 양식코너 -----\n' + tomorrow_sangrok_2f_western_lunch + '\n----- 상록원 뚝배기코너 -----\n' + tomorrow_sangrok_2f_ttukbaegi_lunch, color=0x00ff00)
    tomorrow_sangrokwon2fdinner = discord.Embed(title='내일 상록원 2층 석식 메뉴', description='\n----- 상록원 백반코너 -----\n' + tomorrow_sangrok_2f_bakban_dinner + '\n----- 상록원 일품코너 -----\n' + tomorrow_sangrok_2f_ilpum_dinner + '\n----- 상록원 양식코너 -----\n' + tomorrow_sangrok_2f_western_dinner + '\n----- 상록원 뚝배기코너 -----\n' + tomorrow_sangrok_2f_ttukbaegi_dinner, color=0x00ff00)
    tomorrow_sangrokwon1f = discord.Embed(title='내일 상록원 1층 메뉴', description=tomorrow_sangrok_1f_menu, color=0x00ff00)
    tomorrow_grutergi_lunch = discord.Embed(title='내일 그루터기 중식 메뉴', description='\n----- 그루터기 A코너 -----\n' + tomorrow_grutergi_A_lunch + '\n----- 그루터기 B코너 -----\n' + tomorrow_grutergi_B_lunch + '\n----- 그루터기 PAN -----\n' + tomorrow_grutergi_pan_lunch + '\n----- 그루터기 NOODLE -----\n' + tomorrow_grutergi_noodle_lunch, color=0x00ff00)
    tomorrow_grutergi_dinner = discord.Embed(title='내일 그루터기 석식 메뉴', description='\n----- 그루터기 A코너 -----\n' + tomorrow_grutergi_A_dinner + '\n----- 그루터기 B코너 -----\n' + tomorrow_grutergi_B_dinner + '\n----- 그루터기 PAN -----\n' + tomorrow_grutergi_pan_dinner + '\n----- 그루터기 NOODLE -----\n' + tomorrow_grutergi_noodle_dinner, color=0x00ff00)
    tomorrow_gardencook = discord.Embed(title='내일 가든쿡 메뉴', description='\n----- 가든쿡 샐러드코너 -----\n' + tomorrow_gardencook_salad + '\n----- 가든쿡 파스타코너 -----\n' + tomorrow_gardencook_pasta + '\n----- 가든쿡 리조또코너 -----\n' + tomorrow_gardencook_risotto + '\n----- 가든쿡 볶음밥코너 -----\n' + tomorrow_gardencook_fried_rice + '\n----- 가든쿡 피자코너 -----\n' + tomorrow_gardencook_pizza, color=0x00ff00)
    tomorrow_dormitory_lunch = discord.Embed(title='내일 남산학사(기숙사)식당 중식 메뉴', description='\n----- 남산학사 조식뷔페 -----\n' + tomorrow_dormitory_buffet_breakfast + '\n----- 남산학사 A코너 -----\n' + tomorrow_dormitory_a_lunch + '\n----- 남산학사 B코너 -----\n' + tomorrow_dormitory_b_lunch + '\n----- 남산학사 푸드코트 -----\n' + tomorrow_dormitory_foodcourt_lunch, color=0x00ff00)
    tomorrow_dormitory_dinner = discord.Embed(title='내일 남산학사(기숙사)식당 석식 메뉴', description='\n----- 남산학사 조식뷔페 -----\n' + tomorrow_dormitory_buffet_breakfast + '\n----- 남산학사 A코너 -----\n' + tomorrow_dormitory_a_dinner + '\n----- 남산학사 B코너 -----\n' + tomorrow_dormitory_b_dinner + '\n----- 남산학사 푸드코트 -----\n' + tomorrow_dormitory_foodcourt_dinner, color=0x00ff00)

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
        import time
        secs = time.time()
        tm = time.localtime(secs)
        hour = tm.tm_hour
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
        import time
        secs = time.time()
        tm = time.localtime(secs)
        hour = tm.tm_hour
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
        import time
        secs = time.time()
        tm = time.localtime(secs)
        hour = tm.tm_hour
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

    # elif message.content.startswith('!누리터'):
    #     await message.channel.send(embed=MenuCollection.nuriter)
    #     logger.info("Today's nuriter sent")

    elif message.content.startswith('!남산학사'):
        import time
        secs = time.time()
        tm = time.localtime(secs)
        hour = tm.tm_hour
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

    elif message.content.startswith('!기숙사'):
        import time
        secs = time.time()
        tm = time.localtime(secs)
        hour = tm.tm_hour
        if hour >= 14:
            await message.channel.send(embed=MenuCollection.dormitory_dinner)
            logger.info("Today's dormitory_dinner sent")

        else:
            await message.channel.send(embed=MenuCollection.dormitory_lunch)
            logger.info("Today's dormitory_lunch sent")

    elif message.content.startswith('!석식기숙사'):
        await message.channel.send(embed=MenuCollection.dormitory_dinner)
        logger.info("Today's dormitory_dinner sent")

    elif message.content.startswith('!중식기숙사'):
        await message.channel.send(embed=MenuCollection.dormitory_lunch)
        logger.info("Today's dormitory_lunch sent")

    elif message.content.startswith('!내일상록원3층') or message.content.startswith('내일중식상록원3층'):
        await message.channel.send(embed=MenuCollection.tomorrow_sangrokwon3flunch)
    elif message.content.startswith('!내일상록원2층') or message.content.startswith('내일중식상록원2층'):
        await message.channel.send(embed=MenuCollection.tomorrow_sangrokwon2flunch)
    elif message.content.startswith('!내일상록원1층') or message.content.startswith('내일중식상록원1층'):
            await message.channel.send(embed=MenuCollection.tomorrow_sangrokwon1flunch)
    elif message.content.startswith('!내일그루터기') or message.content.startswith('내일중식그루터기'):
        await message.channel.send(embed=MenuCollection.tomorrow_grutergi_lunch)
    elif message.content.startswith('!내일가든쿡') or message.content.startswith('내일중식가든쿡'):
        await message.channel.send(embed=MenuCollection.tomorrow_gardencook)
    elif message.content.startswith('!내일남산학사') or message.content.startswith('내일중식남산학사'):
        await message.channel.send(embed=MenuCollection.tomorrow_dormitory_lunch)
    elif message.content.startswith('!내일기숙사') or message.content.startswith('내일중식기숙사'):
            await message.channel.send(embed=MenuCollection.tomorrow_dormitory_lunch)
    elif message.content.startswith('내일석식상록원3층'):
            await message.channel.send(embed=MenuCollection.tomorrow_sangrokwon3fdinner)
    elif message.content.startswith('내일석식상록원2층'):
            await message.channel.send(embed=MenuCollection.tomorrow_sangrokwon2fdinner)
    elif message.content.startswith('내일석식상록원1층'):
            await message.channel.send(embed=MenuCollection.tomorrow_sangrokwon1fdinner)
    elif message.content.startswith('내일석식그루터기'):
            await message.channel.send(embed=MenuCollection.tomorrow_grutergi_dinner)
    elif message.content.startswith('내일석식가든쿡'):
            await message.channel.send(embed=MenuCollection.tomorrow_gardencook)
    elif message.content.startswith('내일석식남산학사'):
            await message.channel.send(embed=MenuCollection.tomorrow_dormitory_dinner)
    elif message.content.startswith('내일석식기숙사'):
            await message.channel.send(embed=MenuCollection.tomorrow_dormitory_dinner)

    elif message.content.startswith('!동식아'):
        embed = discord.Embed(title="동국대도 식후경 봇 명령어", description='!상록원3층\n!상록원2층\n!상록원1층\n!그루터기\n!가든쿡\n!남산학사(!기숙사)\n!만든사람', color=0x00ff00)
        await message.channel.send(embed=embed)
        await message.channel.send('자세한 설명은 !동식명령어 에서 확인하실 수 있습니다.')
        logger.info("Help requested")

    elif message.content.startswith('!동식명령어'):
        detail_help_embed = discord.Embed(title="동국대도 식후경 봇 고급명령어", description='!중식0000 or !석식0000을 통해 중식혹은 석식을 확인할 수 있습니다.\n(기본적으로는 시간에 따라 알맞는 메뉴를 보여줍니다.) ex)!석식상록원3층\n!내일0000을 통해 내일 식단을 확인할 수 있습니다.\nex)!내일상록원3층\nex)!내일석식남산학사', color=0x00ff00)
        await message.channel.send(embed=detail_help_embed)
        logger.info("Detailed help requested")

    elif message.content.startswith('!만든사람'):
        developer_embed = discord.Embed(title='동국대도 식후경', description='동국대학교 컴퓨터공학과 19학번 조양진\n버그문의는 깃헙 이슈 혹은 이메일로 부탁드려요.\nhttps://github.com/sheepjin99/Discord_DGUcafeteria\nEmail:7033942cyj@dgu.ac.kr', color=0xffdc6a)
        await message.channel.send(embed=developer_embed)
        await message.channel.send('!엘프사이콩그루')
        logger.info("Credit requested")

    elif message.content.startswith('!엘프사이콩그루'):
        add = random.random()
        adder = random.random()
        divergence = add + adder
        if divergence > 2.0:
            divergence -= 1.0
        divergence = round(divergence, 6)
        divergence = str(divergence)
        diver_embed = discord.Embed(title="현재 세계선 다이버전스", description=divergence+'%', color=0xffdc6a)
        await message.channel.send(embed=diver_embed)

client.run('token')