import pyspeedtest
import datetime


print("***CHECKING CONNECTION PLEASE WAIT***")
#Enter your test server URL
date = datetime.datetime.today().replace(microsecond=0)
test_server = ("www.google.co.in")
tester = pyspeedtest.SpeedTest(test_server)
download = tester.download()
ping = tester.ping()

#Converts the Float to Int
d = int(download)//1024.0/8
p = int(ping)

#4k streaming best number mbps
four_k = 5

print("Using server -", test_server, "On", date)
print("Your Results are...")
print("Ping to server is -", p, "ms")
print("Ping to Download speed is -", d, "MB/s")
if d > four_k:
    print("Your connection is also good for streaming 4K content")
else:
    print("Your connection is not capable of streaming 4K content")
    print("***TEST COMPLETE***")

