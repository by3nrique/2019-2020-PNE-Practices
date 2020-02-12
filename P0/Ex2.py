from Seq0 import *

FOLDER = "../Session-04/"
filename = "U5.txt"
length_bases = 20
print("DNA file: " + filename)
print("The first ", length_bases, "bases are:")
print(seq_read_fasta(FOLDER + filename)[:length_bases])
