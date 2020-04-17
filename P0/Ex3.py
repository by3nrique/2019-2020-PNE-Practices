from Seq0 import *  # We import the functions from Seq0.py

FOLDER = "../Session-04/"  # Obtaining the gene files from this folder
files_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]  # List of genes

print("-----| Exercise 3 |------")
for file in files_list:  # We go throw every file in the list , U5 , ADA...
    sequence = seq_read_fasta(FOLDER + file + ".txt")  # Add the folder and .txt to read properly the file
    print("Gene " + file + " ---> Length: ", seq_len(sequence))  # This function returns the length of a string
