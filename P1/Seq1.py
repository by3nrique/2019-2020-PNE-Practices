import pathlib
class Seq:
    """A class for representing sequence objects"""

    def __init__(self, strbases="NULL"):
        if strbases == "NULL":
            print("NULL Seq Created")
            self.strbases = "NULL"
            self.length = 0
        else:
            v = True
            i = 0
            while i < len(strbases) and v:
                if (strbases[i] != "A") and (strbases[i] != "C") and (strbases[i] != "G") and (strbases[i] != "T"):
                    v = False
                    self.strbases = "ERROR"
                    self.length = 0
                    print("INCORRECT Sequence detected")
                else:
                    i += 1

            if v and strbases != "NULL":
                print("New sequence created!")
                self.strbases = strbases
                self.length = len(self.strbases)

    def __str__(self):
        return self.strbases

    def len(self):
        return self.length

    def count_base(self, base):
        return self.strbases.count(base)

    def count(self):
        bases = ["A", "C", "T", "G"]
        count_bases = []
        for base in bases:
            count_bases.append(self.count_base(base))
        dictionary = dict(zip(bases, count_bases))
        return dictionary

    def reverse(self):
        if not len(self.strbases) and not self.len():
            return self.strbases
        elif not self.len():
            return self.strbases
        else:
            return self.strbases[::-1]

    def complement(self):
        if not len(self.strbases) and not self.len():
            return self.strbases
        elif not self.len():
            return self.strbases
        else:
            bases = ["A", "C", "T", "G"]
            bases_complementary = ["T", "G", "A", "C"]
            dict_bases_complemenytary = dict(zip(bases, bases_complementary))
            complementary = ""
            for i in self.strbases:
                for base, bases_co in dict_bases_complemenytary.items():
                    if i == base:
                        complementary += bases_co
            return complementary

    def read_fasta(self, filename):
        file_contents = pathlib.Path(filename).read_text().split('\n')[1:]
        new_file = "".join(file_contents)
        self.strbases = new_file
        self.length = len(self.strbases)
