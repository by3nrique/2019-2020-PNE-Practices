from Seq0 import *  # We import the functions from Seq0.py

print("-----| Exercise 6 |------")

FOLDER = "../Session-04/"  # Obtaining the gene files from this folder
filename = "U5.txt"
number_of_bases = 20
sequence = seq_read_fasta(FOLDER + filename)  # This function reads a file and return it's content

# -- Printing the information

print("Gene " + filename)
print("Frag:", sequence[:number_of_bases])  # print from the beginning until the limit we want (number of bases)
print("Rev:", seq_reverse(sequence[:number_of_bases]))  # Returns the reverse of a string
