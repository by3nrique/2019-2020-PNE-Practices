from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters server 1
IP = "127.0.0.1"
PORT1 = 8080
PORT2 = 8081
FOLDER = "../Session-04/"
filename = FOLDER + 'FRAT1.txt'

s = Seq()
s.read_fasta(filename)

# Creating fragments
fragments = []
for fragment in range(1, 10):
    fragments.append(f'Fragment {fragment}: ')

index_sequence = 0
index_fragment = 0
while index_fragment < len(fragments):
    sequence = str(s)
    fragments[index_fragment] += sequence[index_sequence]
    index_sequence += 1
    if index_sequence % 10 == 0:
        index_fragment += 1

# connect
c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)
c1.talk('Sending FRAT1 Gene to the Server , in fragments of 10 bases...')
c2.talk('Sending FRAT1 Gene to the Server , in fragments of 10 bases...')

r = 0
while r < len(fragments):
    if r % 2 == 0 or r == 0:
        c1.talk(fragments[r])
    else:
        c2.talk(fragments[r])

    r += 1

# print

print("Gene FRAT1:", s)
for frag in fragments:
    print(frag)
