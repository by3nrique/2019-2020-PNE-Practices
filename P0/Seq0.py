import pathlib  # Import pathlib library for reading files


def seq_ping():  # This function prints OK! in the terminal
    print("OK!")


def seq_read_fasta(filename):  # This function reads a file and return it's content
    # -- Open and read the file
    file_contents = pathlib.Path(filename).read_text().split("\n")[1:]  # [1:] We skip the first line
    body = "".join(file_contents)  # We join all the lines in the same string
    return body


def seq_len(seq):  # This function returns the length of a string
    return len(seq)


def seq_count_base(seq, base):  # This function counts just one base
    return seq.count(base)


def seq_count(seq):  # This function counts the number of bases in a sequence in a dictionary
    bases = ["A", "C", "T", "G"]  # List of bases
    count_bases = []
    for base in bases:  # Go throw every base in list of bases
        count_bases.append(seq_count_base(seq, base))  # Append the counting information to a list
    dictionary = dict(zip(bases, count_bases))  # Create a dictionary from two lists
    return dictionary


def seq_reverse(seq):  # Returns the reverse of a string
    return seq[::-1]  # [::-1] Slicing --> reverse string


def seq_complement(seq):  # Returns a complementary DNA sequence
    bases = ["A", "C", "T", "G"]
    bases_complementary = ["T", "G", "A", "C"]
    dict_bases_complementary = dict(zip(bases, bases_complementary))
    # Create a dictionary  with the shape {base : complementary}
    complementary = ""
    for i in seq:  # Go throw every character in the sequence
        for base, bases_co in dict_bases_complementary.items():
            # .items() gets the keys and values from a dictionary
            if i == base:  # Example if A == A we add the complementary T to the complementary string
                complementary += bases_co

    return complementary  # Return the final complementary sequence
