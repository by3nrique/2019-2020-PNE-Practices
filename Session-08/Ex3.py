import socket

# SERVER IP, PORT
PORT = 8081
IP = "10.3.35.198"

while True:
    # -- Ask the user for the message
    msg_user = input("Type your message: ")

    # -- Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # -- Establish the connection to the Server
    s.connect((IP, PORT))

    # -- Send the user message
    s.send(str.encode(str(msg_user)))

    # -- Close the socket
    s.close()
