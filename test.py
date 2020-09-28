import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
import re
import time
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
r = requests.get('https://www.amazon.com/gp/bestsellers/books/ref=zg_bs_pg_', headers=headers)#, proxies=proxies)
content = r.content
soup = BeautifulSoup(content)

print("entra0")

#for d in soup.findAll('div', attrs={'class':'a'}):
for d in soup.findAll('div', attrs={'class':'a-section a-spacing-none aok-relative'}, recursive=True):
    print(d)
#for d in soup.findAll('div', recursive=True):
    
