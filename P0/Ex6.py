from Seq0 import *

print("-----| Exercise 6 |------")

FOLDER = "../Session-04/"
filename = "U5.txt"
length_bases = 20
sequence = seq_read_fasta(FOLDER + filename)

print("Gene " + filename)
print("Frag:" , (sequence)[:length_bases])
print("Rev:" , seq_reverse(sequence[:length_bases]))

