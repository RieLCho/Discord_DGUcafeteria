# made by Yangjin Cho.
# Check for latest release at https://github.com/sheepjin99/DonggukCafeteria/releases.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
def parse_dgu_coop(index):
    day_of_week = datetime.datetime.today().weekday()+3
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
        result = "데이터가 없습니다 ㅠㅜ"
    return result