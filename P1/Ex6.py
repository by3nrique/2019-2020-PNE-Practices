from Seq1 import Seq

print("-----| Practice 1, Exercise 6 |------")

# -- Create a Null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

bases = ["A", "T", "G", "C"]
print("Sequence 1: (Length : ", s1.len(), ")", s1)
print("Bases:", s1.count())

print("Sequence 2: (Length : ", s2.len(), ")", s2)
print("Bases:", s2.count())

print("Sequence 3: (Length : ", s3.len(), ")", s3)
print("Bases:", s3.count())
