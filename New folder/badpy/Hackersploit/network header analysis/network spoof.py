import os
import sys
import binascii
import struct
import socket

sock_created=False
sniffer_socket= 0

def main():
    global sock_created
    global sniffer_socket
    if sock_created == False:
        sniffer_socket=socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0003))