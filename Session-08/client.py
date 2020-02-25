import socket


PORT = 8080
IP = "212.128.253.128"


# create the socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server
s.connect((IP, PORT))

s.send(str.encode  "))

s.close()