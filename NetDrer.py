#!/usr/bin/python3
import scapy.all as scapy
import optparse as pars

#1- ARPrequest
#2- Brodcast
#3- ARPresponse

def GetParse():
    p_ob = pars.OptionParser()
    p_ob.add_option("-r", "--iprange", dest="ipRange", help="IP range to be scanned")
    # p_ob.add_option("-f", "--destmacfield", dest="dest", help="Brodcast mac adress(default=ff:ff:ff:ff:ff:ff)")
    (uInputs, args) = p_ob.parse_args()

    if not uInputs.ipRange:
        print("Enter IP Range")

    return uInputs


def Nscan(ipRange):

    arpR = scapy.ARP(pdst=ipRange)
    #scapy.ls(scapy.ARP())
    brodcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())

    combinedP = brodcast/arpR
    (answered, unanswered) = scapy.srp(combinedP, timeout=1)
    answered.summary()

ipranger = GetParse()
Nscan(ipranger.ipRange)