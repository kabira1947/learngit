import requests

url= input("enter url with parameter: ")
response= requests.get(url+"'").text
if 'error' in response and 'syntax 'in response or 'MySQL' in response:
    print("it's sql injection vulnerable: ")
else:
    print("it is not sql injection vulnerable")
