# made by Yangjin Cho.
# Check for latest release at https://github.com/sheepjin99/DonggukCafeteria/releases.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime

counter = 0
def parse_dgu_coop(index):
    day_of_week = datetime.datetime.today().weekday()+2
    # Sun = 2, Mon = 3, Tue = 4, Wen = 5, Thu = 6, Fri = 7, Sat = 8 (td index)

    html = urlopen('https://dgucoop.dongguk.edu/store/store.php?w=4&l=2&j=0')  # ex) j=-1 one week before
    source = html.read()
    html.close()

    tasty_soup = BeautifulSoup(source, "lxml")
    table_div = tasty_soup.find(id="sdetail")  # menu table is inside sdetail div
    tables = table_div.find_all("table")
    menu_table = tables[1]  # first table is the menu table what we are looking for
    menu_tr = menu_table.find_all('tr')  # tr number will be index of cafeteria

    cafeteria = menu_tr[index]
    menu_td = cafeteria.find_all('td')
    result = str(menu_td[day_of_week].span.text)
    if result is "":
        result = "데이터가 없습니다."
    global counter
    counter -= -1
    print('DonggukCafeteria.py: Module load OK.'+ '['+str(counter)+'/41]')

    return result


sangrokwon3flunch = ('상록원 3층 중식 메뉴입니다.\n----- 상록원 집밥 -----\n'+parse_dgu_coop(
    2)+'\n----- 상록원 한그릇 -----\n'+parse_dgu_coop(
    4)+'\n----- 상록원 채식당 -----\n'+parse_dgu_coop(6))
sangrokwon3fdinner = ('상록원 3층 석식 메뉴입니다.\n----- 상록원 집밥 -----\n' + parse_dgu_coop(
    3) + '\n----- 상록원 한그릇 -----\n' + parse_dgu_coop(
    5) + '\n----- 상록원 채식당 -----\n' + parse_dgu_coop(6))
sangrokwon2flunch = ('상록원 2층 중식 메뉴입니다.\n----- 상록원 백반코너 -----\n' + parse_dgu_coop(
    8) + '\n----- 상록원 일품코너 -----\n' + parse_dgu_coop(
    10) + '\n----- 상록원 양식코너 -----\n' + parse_dgu_coop(
    12) + '\n----- 상록원 뚝배기코너 -----\n' + parse_dgu_coop(14))
sangrokwon2fdinner = ('상록원 2층 석식 메뉴입니다.\n----- 상록원 백반코너 -----\n' + parse_dgu_coop(
    9) + '\n----- 상록원 일품코너 -----\n' + parse_dgu_coop(
    11) + '\n----- 상록원 양식코너 -----\n' + parse_dgu_coop(
    13) + '\n----- 상록원 뚝배기코너 -----\n' + parse_dgu_coop(15))
sangrokwon1f = ('상록원 1층 메뉴입니다.\n'+parse_dgu_coop(17))
grutergi_lunch = ('그루터기 석식 메뉴입니다.\n----- 그루터기 A코너 -----\n' + parse_dgu_coop(
    26) + '\n----- 그루터기 B코너 -----\n' + parse_dgu_coop(
    28) + '\n----- 그루터기 PAN -----\n' + parse_dgu_coop(
    29) + '\n----- 그루터기 NOODLE -----\n' + parse_dgu_coop(30))
grutergi_dinner = ('그루터기 석식 메뉴입니다.\n----- 그루터기 A코너 -----\n' + parse_dgu_coop(
    25) + '\n----- 그루터기 B코너 -----\n' + parse_dgu_coop(
    27) + '\n----- 그루터기 PAN -----\n' + parse_dgu_coop(
    29) + '\n----- 그루터기 NOODLE -----\n' + parse_dgu_coop(30))
gardencook = ('가든쿡 메뉴입니다.\n----- 가든쿡 샐러드코너 -----\n' + parse_dgu_coop(
    32) + '\n----- 가든쿡 파스타코너 -----\n' + parse_dgu_coop(
    33) + '\n----- 가든쿡 리조또코너 -----\n' + parse_dgu_coop(
    34) + '\n----- 가든쿡 볶음밥코너 -----\n' + parse_dgu_coop(
    35) + '\n----- 가든쿡 피자코너 -----\n' + parse_dgu_coop(36))
nuriter = ('누리터식당(일산) 메뉴입니다.\n----- 누리터 조식뷔페 -----\n' + parse_dgu_coop(
    40) + '\n----- 누리밥상 중식메뉴 -----\n' + parse_dgu_coop(
    41) + '\n----- 누리밥상 석식메뉴 -----\n' + parse_dgu_coop(
    42) + '\n----- 누리터 더진국 -----\n' + parse_dgu_coop(
    43) + '\n----- 누리터 팬앤누들 -----\n'+ parse_dgu_coop(44))
dormitory_lunch = ('남산학사(기숙사)식당 중식 메뉴입니다.\n----- 남산학사 조식뷔페 -----\n' + parse_dgu_coop(
    46) + '\n----- 남산학사 A코너 -----\n' + parse_dgu_coop(
    47) + '\n----- 남산학사 B코너 -----\n' + parse_dgu_coop(
    49) + '\n----- 남산학사 푸드코트 -----\n' + parse_dgu_coop(51))
dormitory_dinner = ('남산학사(기숙사)식당 석식 메뉴입니다.\n----- 남산학사 조식뷔페 -----\n' + parse_dgu_coop(
    46) + '\n----- 남산학사 A코너 -----\n' + parse_dgu_coop(
    48) + '\n----- 남산학사 B코너 -----\n' + parse_dgu_coop(
    50) + '\n----- 남산학사 푸드코트 -----\n' + parse_dgu_coop(51))

print('DonggukCafeteria.py: Menu variables load OK.')