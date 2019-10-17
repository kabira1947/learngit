import requests
import bs4
import parser

res = requests.get('http://www.prabhukalyansamal.esy.es')
print(type(res))
print(res.text)
soup = parser(res.text,'html')
#soup = bs4.BeautifulSoup(res.text,'html')
print(type(soup))
print(soup.select('title'))
print(soup.select('.collapse'))
for i in soup.select('.p'):
    print(i.text)