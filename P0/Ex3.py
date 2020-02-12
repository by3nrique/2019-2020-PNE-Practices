from Seq0 import *

FOLDER = "../Session-04/"
files_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

print("-----| Exercise 3 |------")
for file in files_list:
    sequence = seq_read_fasta(FOLDER + file + ".txt")
    print("Gene " + file + " ---> Length: ", seq_len(sequence))
