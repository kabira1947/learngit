from selenium import webdriver
import time

username = 'adhwiraj@email.com'
password = 'premalata@1995'

url = 'https://www.facebook.com/'

driver = webdriver.Chrome("C://Program Files (x86)//Google//Chrome//Application//chrome.exe")

driver.get(url)

driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)

time.sleep(20)

driver.find_element_by_id('loginbutton').click()
