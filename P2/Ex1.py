from Client0 import Client

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# SERVER
IP = "127.0.0.1"
PORT = 8080

# Create client object with the Client0 class
c = Client(IP, PORT)

# Test
c.ping()

# Print the IP and PORTs
print(f"IP: {c.ip}, {c.port}")
