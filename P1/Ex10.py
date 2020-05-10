from Seq1 import Seq  # Import our Seq class

print("-----| Practice 1, Exercise 10 |------")

FOLDER = "../Session-04/"  # Obtaining the gene files from this folder
bases = ["A", "C", "T", "G"]
files_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]  # List of genes

for file in files_list:  # We go throw every file in the list , U5 , ADA...
    s = Seq()  # Create a Seq object
    s.read_fasta(FOLDER + file + ".txt")

    # This function reads a file and return it's content
    # Add the folder and .txt to read properly the file
    dict_bases = s.count()

    min_value = 0  # Set a min value
    best_base = ""
    for base, value in dict_bases.items():
        # .items() gets the keys and values from a dictionary
        while value > min_value:  # With this loop , find the most frecuent base
            min_value = value
            best_base = base
            # Replace the minimun value with the "new minimun value" and the base with this value is set as best_base

    print(f"Gene {file}: Most frequent Base: {best_base}")
