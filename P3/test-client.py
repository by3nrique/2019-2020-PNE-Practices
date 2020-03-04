from Client0 import Client
from Seq1 import Seq

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters
IP = "127.0.0.1"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)

print("Connection to SERVER at" , IP , ", PORT: " , PORT)

print ("* Testing GET...")
c.talk("GET 0")
c.talk("GET 1")
c.talk("GET 2")
c.talk("GET 3")
c.talk("GET 4")

seq = Seq("ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")

print ("* Testing INFO...")
print ("Sequence: " ,seq )
print("Total length: " , seq.len())
c.talk(str("TALK" + seq))


print ("* Testing COMP...")
print ("* Testing REV...")
print ("* Testing GENE...")
