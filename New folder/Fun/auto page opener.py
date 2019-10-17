import webbrowser
import time
import random

while True:
    sites= random.choice(['google.co.in','weforyourlife.xyz','facebook.com','youtube.com'])
    visit ="http://{}".format(sites)
    webbrowser.open(visit)
    seconds=random.randrange(5,30)
    time.sleep(seconds)