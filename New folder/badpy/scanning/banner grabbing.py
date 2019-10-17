
# Usages :
usage = "usage: %prog [options] "
# Version
Version="%prog 1"


import socket
import sys
import time


def banner_grab(ip,port):
    try:
        s=socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        print(ip+ " : "+port)
    except:
        return
def vuln(banner):
    if len(sys.argv) >=1:
        filename= sys.argv[1]
        for line in filename.readlines():
            line=line.strip("\n")
            if banner in line:
                print("%s is vulnerable." %banner)
            else:
                print("%s is not vulnerable" %banner)
def main():
    ports= [21,22,80,443]

    for p in range(0,5):
        for port in ports:
            ip= "49.35.31.18"#+str(p)
            banner_grab(ip,port)
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Thank for using")
        sys.exit(0)
    except Exception as e:
        print(e)