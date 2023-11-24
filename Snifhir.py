#!/usr/bin/python3
import scapy.all as scapy
from scapy_http import http

def listenPs(interface):
    scapy.sniff(iface=interface, store=False, prn=analyzePs)
    #prn : callback function

def analyzePs(packet):
    #packet.show()
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)

interface = str(input("Interface: "))
listenPs(interface)

