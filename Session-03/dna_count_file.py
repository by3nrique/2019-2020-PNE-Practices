import pathlib  # Import pathLib

# The filename to open
FILENAME = "DNA.txt"

# open and read the file
file_contents = pathlib.Path(FILENAME).read_text().split("\n")[1:]  # Split lines and skip the first one [1:]
dna_sequence = "".join(file_contents)  # Join all the list in the same string without spaces


def count(dna_seq):  # This function counts the number of bases
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


print("Total length is: ", len(dna_sequence))  # Print the length of the sequence
print("A: ", count(dna_sequence)[0], "C: ", count(dna_sequence)[1], "T:", count(dna_sequence)[2], "G: ",
      count(dna_sequence)[3])
