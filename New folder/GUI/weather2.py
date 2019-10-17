import requests

api_address='http://api.openweathermap.org/data/2.5/weather?appid=70cfa302d957ee0b76e02ba5bc699eb8&q='
city = input('City Name :')
url = api_address + city
json_data = requests.get(url).json()
format_add = json_data['base']
print(format_add)