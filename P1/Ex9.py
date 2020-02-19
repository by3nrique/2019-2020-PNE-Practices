from Seq1 import Seq

print("-----| Practice 1, Exercise 9 |------")
folder = "../Session-04/"
filename = folder + 'U5.txt'
s = Seq()
s.read_fasta(filename)

print(f"Sequence : (Length: {s.len()}) {s}")
print("\tBases: ", s.count())
print("\tRev: ", s.reverse())
print("\tComp:", s.complement())
