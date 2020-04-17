from Seq0 import *  # We import the functions from Seq0.py

print("-----| Exercise 5 |------")

FOLDER = "../Session-04/"  # Obtaining the gene files from this folder
bases = ["A", "C", "T", "G"]
files_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]  # List of genes

for file in files_list:  # We go throw every file in the list , U5 , ADA...
    sequence = seq_read_fasta(FOLDER + file + ".txt")  # Add the folder and .txt to read properly the file
    print("Gene " + file, seq_count(sequence))  # This function counts the number of bases in a sequence
