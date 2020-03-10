dna_sequence = input("Introduce the sequence: ")


def count(dna_seq):
    a = 0
    g = 0
    t = 0
    c = 0
    for base in dna_seq:
        if base == "A":
            a += 1
        elif base == "G":
            g += 1
        elif base == "T":
            t += 1
        elif base == "C":
            c += 1
    return a, c, t, g


print("Total length is: ", len(dna_sequence))
print("A: ", count(dna_sequence)[0], "C: ", count(dna_sequence)[1], "T:", count(dna_sequence)[2], "G: ",
      count(dna_sequence)[3])