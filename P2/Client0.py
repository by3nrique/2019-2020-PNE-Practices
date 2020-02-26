# Class for sending messages easily to the server
import socket
import termcolor


def ping():
    print("OK!")


class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = int(port)

    def __str__(self):
        return "Connection to SERVER at " + self.ip + " , PORT: " + str(self.port)

    def talk(self, msg):
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))
        # Send data.
        s.send(str.encode(str(msg)))
        # Receive data
        response = s.recv(2048).decode("utf-8")
        # Close the socket
        s.close()
        # Return the response
        return response

    def debug_talk(self, msg):
        message = str(msg)
        response = self.talk(msg)
        print("To Server: ", end="")
        termcolor.cprint(message, 'green')
        print("From Server: ", end="")
        termcolor.cprint(response, 'blue')
