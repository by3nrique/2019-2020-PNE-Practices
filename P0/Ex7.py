from Seq0 import *  # We import the functions from Seq0.py

print("-----| Exercise 7 |------")

FOLDER = "../Session-04/"  # Obtaining the gene files from this folder
filename = "U5.txt"
number_of_bases = 20
sequence = seq_read_fasta(FOLDER + filename)  # This function reads a file and return it's content

# -- Printing the information
# print from the beginning until the limit we want (number of bases)
print("Gene " + filename)
print("Frag:", sequence[:number_of_bases])
print("Rev:", seq_complement(sequence[:number_of_bases]))  # Returns a complementary DNA sequence
