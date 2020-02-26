from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters
IP = "10.3.34.194"
PORT = 8081
FOLDER = "../Session-04/"
filename = FOLDER + 'U5.txt'
s = Seq()
s.read_fasta(filename)

# -- Create a client object
c = Client(IP, PORT)

c.debug_talk("Sending the U5 Gene to the server..")
c.debug_talk(s)
