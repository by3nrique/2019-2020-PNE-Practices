from Seq0 import *

print("-----| Exercise 5 |------")

FOLDER = "../Session-04/"
bases = ["A", "C", "T", "G"]
files_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

for file in files_list:
    sequence = seq_read_fasta(FOLDER + file + ".txt")
    print("Gene " + file , seq_count(sequence))
