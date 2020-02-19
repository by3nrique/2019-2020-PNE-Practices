class Seq:
    """A class for representing sequence objects"""

    def __init__(self, strbases):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        v = True
        i = 0
        while i < len(strbases) and v:
            if (list(strbases[i]) != "A") and (list(strbases[i]) != "C") and (list(strbases[i]) != "G") and (list(strbases[i]) != "T"):
                v = False
                print ("INCORRECT Sequence detected")
            else:
                i += 1
        if v == True:
            print("This is a valid DNA sequence")
            self.strbases = strbases

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

class Gene(Seq):
    """This class is derived from the Seq Class
       All the objects of class Gene will inherite
       the methods from the Seq class
    """
    pass

# - - Main program
# Create objects of the class Seq
s1 = Seq("AGTACACTGGT")
g = Gene("CGTAACP")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"  Length: {s1.len()}")
print(f"Sequence 2: {g}")
print(f"  Length: {g.len()}")
print("Testing objects....")