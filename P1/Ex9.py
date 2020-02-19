from Seq1 import Seq

print("-----| Practice 1, Exercise 9 |------")

FOLDER = "../Session-04/"
FILENAME = FOLDER + "U5.txt"
# -- Create a Null sequence
s = Seq()

# -- Initialize the null seq with the given file in fasta format
s.read_fasta(FILENAME)

print("Sequence 1: (Length : ", s.len(), ")", s)
print("Bases:", s.count())
print("Rev:", s.reverse())
print("Comp:", s.complement())