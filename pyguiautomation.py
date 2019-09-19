import pyautogui as p

p.FAILSAFE = True

for i in range(10):
    p.moveTo(500,100,duration=0.1)
    p.moveTo(600,100,duration=0.1)
    p.moveTo(500,200,duration=0.1)
    p.moveTo(600,200,duration=0.1)
