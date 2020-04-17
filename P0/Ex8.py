from Seq0 import *  # We import the functions from Seq0.py

print("-----| Exercise 8 |------")

FOLDER = "../Session-04/"  # Obtaining the gene files from this folder
bases = ["A", "C", "T", "G"]
files_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]  # List of genes

for file in files_list:  # We go throw every file in the list , U5 , ADA...
    sequence = seq_read_fasta(FOLDER + file + ".txt")
    # This function reads a file and return it's content
    # Add the folder and .txt to read properly the file
    dict_bases = seq_count(sequence)
    # seq_count()
    # This function counts the number of bases in a sequence in a dictionary
    min_value = 0  # Set a min value
    best_base = ""
    for base, value in dict_bases.items():
        # .items() gets the keys and values from a dictionary
        while value > min_value:  # With this loop , find the most frecuent base
            min_value = value
            best_base = base
            # Replace the minimun value with the "new minimun value" and the base with this value is set as best_base

    print("Gene", file, " : Most frequent Base: ", best_base)
