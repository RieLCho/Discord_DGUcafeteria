import urllib.request
import numpy as np
import pandas as pd
from html_table_parser import HTMLTableParser

target = 'https://dgucoop.dongguk.edu/store/store.php?w=4&l=2&j=-13'

# get website content
req = urllib.request.Request(url=target)
f = urllib.request.urlopen(req)
xhtml = f.read().decode('euc-kr')

# instantiate the parser and feed it
p = HTMLTableParser()
p.feed(xhtml)
print(p.tables)


