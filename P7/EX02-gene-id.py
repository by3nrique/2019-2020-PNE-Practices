# Import the required libraries
import termcolor as tc

GENES = dict(FRAT1='ENSG00000165879',  # defining the dictionary
             ADA='ENSG00000196839',
             FXN='ENSG00000165060',
             RNU6_269P='ENSG00000212379',
             MIR633='ENSG00000207552',
             TTTY4C='ENSG00000228296',
             RBMY2YP='ENSG00000227633',
             FGFR3='ENSG00000068078',
             KDR='ENSG00000128052',
             ANK2='ENSG00000145362')

# Printing the information
print("Dictionary of Genes!")
print(f"There are {len(GENES)} genes in the dicctionary:\n")

for gene in GENES:  # Go through every gene in the list GENES
    tc.cprint(gene, 'red', end=": --> ")
    print(GENES[gene])
