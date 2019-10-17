'''import urllib.request

url =input('enter the url:')

urllib.request.urlretrieve(url, 'cricket1.jpg')'''

from bs4 import BeautifulSoup
from datetime import datetime as dt
import requests
import urllib.request

res = requests.get('https://bing.gifposter.com/')
soup = BeautifulSoup(res.text, 'lxml')

image = soup.find('img', {'class': 'fl'})


lmg = image['src']

filename = dt.now().strftime('%d-%m-%y')
urllib.request.urlretrieve(lmg, filename)