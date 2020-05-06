from Client0 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# Parameters for the server
IP = "127.0.0.1"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
sequence_test = "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"

print("Connection to SERVER at", IP, ", PORT: ", PORT)

# TEST PING
print("* Testing PING...")
print(c.talk("PING"))

# TEST GET
print("* Testing GET...")
print("GET 0:", c.talk("GET 0"))
print("GET 1:", c.talk("GET 1"))
print("GET 2:", c.talk("GET 2"))
print("GET 3:", c.talk("GET 3"))
print("GET 4:", c.talk("GET 4"))

# TEST INFO
print("* Testing INFO...")
print(c.talk("INFO " + sequence_test))

# TEST COMP
print("* Testing COMP...")
print("COMP " + sequence_test)
print(c.talk("COMP " + sequence_test))

# TEST REV
print("* Testing REV...")
print("REV " + sequence_test)
print(c.talk("REV " + sequence_test))

# TEST REV
print("* Testing GENE...")
files_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for file in files_list:
    print("GENE", file)
    print(c.talk("GENE " + file))
