dna_sequence = input("Introduce the sequence: ")  # The user enters the sequence directly


def count(dna_seq):
    A = 0
    G = 0
    T = 0
    C = 0
    for base in dna_seq:
        if base == "A":
            A += 1  # When there is an "A" we add 1 to the counter A
        elif base == "G":
            G += 1
        elif base == "T":
            T += 1
        elif base == "C":
            C += 1
    return A, C, T, G


print("Total length is: ", len(dna_sequence))
print("A: ", count(dna_sequence)[0], "C: ", count(dna_sequence)[1], "T:", count(dna_sequence)[2], "G: ",
      count(dna_sequence)[3])
