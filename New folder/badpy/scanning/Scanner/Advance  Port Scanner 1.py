from socket import *
import optparse
from termcolor import colored
from threading import *

def connectionScanner(hostip,portn):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        if sock.connect_ex(hostip,portn):
            print(colored("the port %d is closed" %(portn),"red"))
        else:
            print(colored("The port %d is open" %(portn), "blue"))
    except:
            print("unknown Host %s" %hostip)



def portscanner(portn,hostip):
    try:
        IP= gethostbyname(hostip)
    except:
        print("unknown host %s" %hostip)
    try:
        Port= gethostbyaddr(portn)
        print('[+] Scan Results For: ' + portn[0])
    except:
        print('[+] Scan Results For: ' + IP)
    for ports in portn:
        t= Thread(target=connectionScanner,args=(hostip,int(portn)))
        t.start()

    setdefaulttimeout(1)


def main():
    parser= optparse.OptionParser("How to use :" + "-H <Host IP address> -P <Target port number>")
    parser.add_option("-H",dest="hostip",type="string",help="Put the host Ip address")
    parser.add_option("-P", dest="portn", type="string", help="Put the port numbers separated by comma")
    (options,args)=parser.parse_args()
    hostip= options.hostip
    portn=str(options.portn).split(",")
    if (hostip==None) | (portn==None):
        print(parser.usage)
        exit(0)
    portscanner(hostip,portn)

if __name__ == '__main__':
    main()