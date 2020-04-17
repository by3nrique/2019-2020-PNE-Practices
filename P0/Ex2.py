from Seq0 import *  # We import the functions from Seq0.py

FOLDER = "../Session-04/"  # Obtaining the gene files from this folder
filename = "U5.txt"
number_of_bases = 20

# -- Printing the the computations

print("DNA file: " + filename)  # Prints the file used
print("The first ", number_of_bases, "bases are:")
print(seq_read_fasta(FOLDER + filename)[:number_of_bases])
# seq_read_fasta() # This function reads a file and return it's content
# print from the beginning until the limit we want (number of bases)
