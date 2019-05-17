import socket
import sys
import time

s = socket.socket

host = input(str("Please enter the hostname of the server: "))
port = 8080
s.connect((host,port))
print("Connected to chatbot")
while 1:
      incoming_message = s.recv(1024)
      incoming_message = incoming_message.decode()
      print("Server :", incoming_message)
      print("")
