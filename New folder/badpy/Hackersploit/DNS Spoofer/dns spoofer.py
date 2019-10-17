#it changes a certian IP address to different IP address


from scapy.all import *

def findDNS(p):
    if p.haslayer(DNS):
        print(p[IP].src,p[DNS].summery())

sniff(prn=findDNS)