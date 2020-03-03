from seq01 import Seq


def print_seqs(seqs):
    for seq in seqs:
        print("Sequence ", seqs.index(seq), ": (Length : ", seq.len(), ")", seq)


def generate_seqs(base, times):
    seqs_list = []
    for i in range(times):
        seqs_list.append(Seq((i + 1) * base))
    return seqs_list


print("-----| Exercise 3 |------")

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)
