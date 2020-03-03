from seq01 import Seq

print("-----| Exercise 2 |------")

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]


def print_seqs(seqs):
    for seq in seqs:
        print("Sequence ", seqs.index(seq), ": (Length : ", seq.len(), ")", seq)


print_seqs(seq_list)
