from bs4 import BeautifulSoup
import requests

res= requests.get('https://www.cricbuzz.com/cricket-series/2697/icc-cricket-world-cup-2019/points-table')
soup=BeautifulSoup(res.text,'lxml')

table=soup.find('table',{'class':'table cb-srs-pnts'})
list= soup.find('tbody',{'class':'table cb-srs-pnts'})
column=list.find('tr')
for td in column:
    team=td.find('a')[0].text
    #rank=td.find('a')[].text
    point=td.find('a')[6].text
    match=td.find('a')[1].text
    won=td.find('a')[2].text
    lost=td.find('a')[3].text
