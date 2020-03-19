# made by Yangjin Cho.
# Check for latest release at https://github.com/sheepjin99/DonggukCafeteria/releases.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler("MobileDonggukCafeteria.py.log")
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


html = urlopen("http://dgucoop.dongguk.edu/mobile/menu.html?code=5")
logger.info("DGUcoop Website Opened")
source = html.read()
html.close()

def sangrok_3f(tr, td):
    tasty_soup = BeautifulSoup(source, "lxml")
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

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=1')
logger.info("DGUcoop Website Opened")
source = html.read()
html.close()

def sangrok_2f(tr, td):
    tasty_soup = BeautifulSoup(source, "lxml")
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


sangrok_2f_bakban_lunch = sangrok_2f(1,1)
sangrok_2f_bakban_dinner = sangrok_2f(1,2)
sangrok_2f_ilpum_lunch = sangrok_2f(2,1)
sangrok_2f_ilpum_dinner = sangrok_2f(2,2)
sangrok_2f_western_lunch = sangrok_2f(3,1)
sangrok_2f_western_dinner = sangrok_2f(3,2)
sangrok_2f_ttukbaegi_lunch = sangrok_2f(4,1)
sangrok_2f_ttukbaegi_dinner = sangrok_2f(4,2)

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=7')
logger.info("DGUcoop Website Opened")
source = html.read()
html.close()

def sangrok_1f(tr=1, td=1):
    tasty_soup = BeautifulSoup(source, "lxml")
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

sangrok_1f = sangrok_1f()

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=2')
logger.info("DGUcoop Website Opened")
source = html.read()
html.close()

def grutergi(tr, td):
    tasty_soup = BeautifulSoup(source, "lxml")
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

grutergi_A_lunch = grutergi(1,1)
grutergi_A_dinner = grutergi(1,2)
grutergi_B_lunch = grutergi(2,1)
grutergi_B_dinner = grutergi(2,2)

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=0')
logger.info("DGUcoop Website Opened")
source = html.read()
html.close()

def grutergi_pan_noodle(tr, td):
    tasty_soup = BeautifulSoup(source, "lxml")
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

grutergi_pan_lunch = grutergi_pan_noodle(1,1)
grutergi_pan_dinner = grutergi_pan_noodle(1,2)
grutergi_noodle_lunch = grutergi_pan_noodle(2,1)
grutergi_noodle_dinner = grutergi_pan_noodle(2,2)

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=9')
logger.info("DGUcoop Website Opened")
source = html.read()
html.close()

def gardencook(tr, td):
    tasty_soup = BeautifulSoup(source, "lxml")
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

gardencook_salad = gardencook(1, 1)
gardencook_pasta = gardencook(2, 1)
gardencook_risotto = gardencook(3, 1)
gardencook_fried_rice = gardencook(4, 1)
gardencook_pizza = gardencook(5, 1)

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=8')
logger.info("DGUcoop Website Opened")
source = html.read()
html.close()

def dormitory(tr, td):
    tasty_soup = BeautifulSoup(source, "lxml")
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

dormitory_buffet_breakfast = dormitory(1,1)
dormitory_a_lunch = dormitory(2,2)
dormitory_a_dinner = dormitory(2,3)
dormitory_b_lunch = dormitory(3,2)
dormitory_b_dinner = dormitory(3,3)
dormitory_foodcourt_lunch = dormitory(4,2)
dormitory_foodcourt_dinner = dormitory(4,3)

