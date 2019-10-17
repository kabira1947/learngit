import socket
from termcolor import colored
from datetime import datetime
import sys

host= input("Enter the host name: ")
print("Scanning started at :"+ str(datetime.now()))
print("Scanning the target: " + host)


def portscanner(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(2)
    if sock.connect_ex((host,port)):
        print(colored("the port %d is closed" %(port),"red"))
    else:
        print(colored("The port %d is open" %(port), "blue"))
try:
    for port in range(1,10000):
        portscanner(port)
except socket.gaierror:
    print("Host name could not be resoleved")
    sys.exit()
except socket.error:
    print("couldn't connect the socket")
    sys.exit()

#106.193.227.110