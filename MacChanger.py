#!/usr/bin/python2
import subprocess
import optparse
import re


def GetParses():

    p_ob = optparse.OptionParser()
    p_ob.add_option("-i", "--interface", dest="interface", help="Interface to change.")
    p_ob.add_option("-m", "--mac", dest="mac", help="Mac adress to change.")

    return p_ob.parse_args()


def ChangeMac(u_iface, u_mac):

    subprocess.call(["ifconfig", u_iface, "down"])
    subprocess.call(["ifconfig", u_iface, "hw", "ether", u_mac])
    subprocess.call(["ifconfig", u_iface, "up"])
    subprocess.call(["ifconfig", u_iface])

def CMac(interface):

    ifconfig = subprocess.check_output(["ifconfig", interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig)

    if new_mac:
        return new_mac.group(0)
    else:
        return None

print("MacChanger launching...")
try:
    (u_inputs,args) = GetParses()
    ChangeMac(u_inputs.interface, u_inputs.mac)
    lost_proc = CMac(u_inputs.interface)

    if lost_proc == u_inputs.mac:
        print("Mac adress has been changed.")
        print("MacChanger Finishing.")
    else:
        print("Mac adress couldn't be changed!")
except:
    print("MacChanger failed to launch!")
    print("Please input -i(--interface) and -m(--mac)!!")