#time

import time

ticks = time.time()

print(ticks)
#full time

ticks = time.localtime(time.time())

print(ticks)

#current time

ticks = time.asctime(time.localtime(time.time()))

print(ticks)

# calnder
import calendar

ticks= calendar.month(2008,8)
print(ticks)

import time
print(time.altzone)
print(time.localtime())
print(time.gmtime(3505032300)) # calculates form 1970
print(time.asctime(time.gmtime(3505032300)))



#time difference

print(time.asctime())
print(time.ctime())


import time,datetime
dt= datetime.datetime.today()
print('the current time {}/{}/{}:{}'.format(dt.year,dt.month,dt.day,dt.hour))