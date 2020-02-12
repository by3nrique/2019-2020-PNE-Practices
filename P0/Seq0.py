import pathlib


def seq_ping():
    print("OK!")


def seq_read_fasta(filename):
    # -- Open and read the file
    file_contents = pathlib.Path(filename).read_text().split("\n")[1:]
    body = "".join(file_contents)
    return body


def seq_len(seq):
    return len(seq)


def seq_count_base(seq, base):
    return seq.count(base)


def seq_count(seq):
    bases = ["A", "C", "T", "G"]
    count_bases = []
    for base in bases:
        count_bases.append(seq_count_base(seq, base))
    dictionary = dict(zip(bases, count_bases))
    return dictionary


def seq_reverse(seq):
    return seq[::-1]


def seq_complement(seq):
    bases = ["A", "C", "T", "G"]
    bases_complementary = ["T", "G", "A", "C"]
    dict_bases_complemenytary = dict(zip(bases, bases_complementary))
    complementary = ""
    for i in seq:
        for base, bases_co in dict_bases_complemenytary.items():
            if i == base:
                complementary += bases_co

    return complementary
