import pygeoip as p
import requests

#my_ip=input("enter the ip address: ")

a = int(input("please enter 1 or 2: "))

if a == 1:
    print("you selected 1")
    my_ip = input("Enter your ip-address: ")
elif a == 2:
    print("you selected 2")
    my_ip = requests.get("https://api.ipify.org/").text
else:
    print("you have selected "+ str(a) + " and it is not a valid option \n Good Bye!!")
    exit()
geoip = p.GeoIP('GeoLiteCity.dat')

res = geoip.record_by_addr(my_ip)

for key,values in res.items():
    print("%s :%s" %(key,values))

