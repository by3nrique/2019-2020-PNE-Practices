import termcolor
from seq01 import Seq


def print_seqs(seqs, color):
    for seq in seqs:
        termcolor.cprint(("Sequence " + str(seqs.index(seq)) + " : (Length : " + str(seq.len()) + ") " + str(seq)),
                         color)


def generate_seqs(base, times):
    seqs_list = []
    for i in range(times):
        seqs_list.append(Seq((i + 1) * base))
    return seqs_list


print("-----| Exercise 4 |------")

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", "blue")
print_seqs(seq_list1, "blue")

print()
termcolor.cprint("List 2:", "green")
print_seqs(seq_list2, "green")
