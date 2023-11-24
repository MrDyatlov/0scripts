#!/usr/bin/python3
import subprocess

m = input("m: ")

try:
    print("hashscript started!")
    subprocess.call(["hashcat", "-m", m, "0d082c4b4f2aeafb67fd0ea568a997e9d3ebc0eb"])
except:
    print("hashscript failed!")

hash = input("hash: ")

try:
    print("hashscript 2 started!")
    subprocess.call(["hashcat", "--help", "|", "grep", hash])
except:
    print("hashcript 2 failed!")