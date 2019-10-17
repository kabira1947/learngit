from socket import  *
from termcolor import colored
import optparse
from threading import *


def connScan(tghost,tgport):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        if sock.connect_ex((tghost,tgport)):
            print(colored("the port %d is closed" %(tgport),"red"))
        else:
            print(colored("The port %d is open" %(tgport), "blue"))
    except:
            print("unknown Host %s" %tghost)



def portscanner(tgport,tghost):
    try:
        Ip= gethostbyname(tghost)
    except:
        print("unknown host %s" %tghost)
    try:
         port = gethostbyaddr(tgport)
         print('[+] Scan Results for: ' + port[0])
    except:
         print('[+] Scan Results FOR: ' + Ip)
    setdefaulttimeout(1)
    for ports in tgport:
        t=Thread(target=connScan,args=(tghost,int(tgport)))
        t.start()


def main():
    parser = optparse.OptionParser("Syntax"+"-H <target host> -p <target port>")
    parser.add_option("-H",dest='tghost',type='string',help='specify target host')
    parser.add_option("-p", dest='tgport', type='string', help='specify target ports separated by comma')
    (options, args) = parser.parse_args()
    tghost = options.tghost
    tgport = str(options.tgport).split('.')
    if (tghost== None) | (tgport[0]==None):
        print(parser.usage)
        exit(0)
    portscanner(tgport,tghost)
if __name__ == '__main__':
    main()