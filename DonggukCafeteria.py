# made by Yangjin Cho.
# Check for latest release at https://github.com/sheepjin99/DonggukCafeteria/releases.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import logging

counter = 0

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler("DonggukCafeteria.py.log")
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

html = urlopen('https://dgucoop.dongguk.edu/store/store.php?w=4&l=2&j=0')# ex) j=-1 one week before
logger.info("dgucoop url opened")
source = html.read()
html.close()
logger.info("dgucoop url closed")

def parse_dgu_coop(index, day_of_week=0):
    logger.info("parse_dgu_coop function start")
    day_of_week += datetime.datetime.today().weekday() + 3
    # Sun = 2, Mon = 3, Tue = 4, Wen = 5, Thu = 6, Fri = 7, Sat = 8 (td index)
    if index is 3:  # 석식 메뉴의 경우 -1
        day_of_week -= 1
    elif index is 5:
        day_of_week -= 1
    elif index is 26:
        day_of_week -= 1
    elif index is 28:
        day_of_week -= 1
    elif index is 42:
        day_of_week -= 1
    elif index is 48:
        day_of_week -= 1
    elif index is 50:
        day_of_week -= 1
    elif index is 9:
        day_of_week -= 1
    elif index is 11:
        day_of_week -= 1
    elif index is 13:
        day_of_week -= 1
    elif index is 15:
        day_of_week -= 1
    elif index is 6:
        day_of_week -= 1
    elif index is 29:
        day_of_week -= 1
    elif index is 30:
        day_of_week -= 1
    elif index is 32:
        day_of_week -= 1
    elif index is 33:
        day_of_week -= 1
    elif index is 34:
        day_of_week -= 1
    elif index is 35:
        day_of_week -= 1
    elif index is 36:
        day_of_week -= 1
    elif index is 43:
        day_of_week -= 1
    elif index is 44:
        day_of_week -= 1
    elif index is 51:
        day_of_week -= 1

    tasty_soup = BeautifulSoup(source, "lxml")
    table_div = tasty_soup.find(id="sdetail")  # menu table is inside sdetail div
    try:
        tables = table_div.find_all("table")
    except AttributeError:
        pass
    menu_table = tables[1]  # second table is the menu table what we are looking for
    menu_tr = menu_table.find_all('tr')  # tr number will be index of cafeteria
    try:
        cafeteria = menu_tr[index]
    except IndexError:
        cafeteria = []

    try:
        menu_td = cafeteria.find_all('td')
    except AttributeError:
        pass

    try:
        result = str(menu_td[day_of_week].span.text)
    except UnboundLocalError:
        result = "데이터가 없습니다."
    # try:
    #     result = str(menu_td[day_of_week].span.text)
    # except AttributeError:
    #     result = ''

    if result is "":
        result = "데이터가 없습니다."
    global counter
    counter -= -1
    print('DonggukCafeteria.py: Module load OK.' + '[' + str(counter) + '/41]')
    logger.info("parse_dgu_coop function end")
    return result
