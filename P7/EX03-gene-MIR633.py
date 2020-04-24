# Import the required libraries
import http.client
import json
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

gene = 'MIR633'

server = 'rest.ensembl.org'  # Server address
endpoint = '/sequence/id/' + GENES[gene]  # This endpoint returns a sequence
options = '?content-type=application/json'  # We will get json information
method = "GET"  # We will only use the GET method
URL = server + endpoint + options

# Print the connection information
tc.cprint(f"\nConnecting to server: {server}", 'blue')
tc.cprint(f"URL : {URL}", 'blue')

# Connect w the server
connection = http.client.HTTPConnection(server)

try:
    connection.request(method, endpoint + options)
except ConnectionRefusedError:  # If the connection fail we print an error message
    print("ERROR! Cannot connect to the Server")
    exit()

# response and status
response = connection.getresponse()
# .getresponse() method that returns the response information from the server

tc.cprint(f"Response received!: {response.status} {response.reason}\n", 'blue')

data = response.read().decode("utf-8")  # It is necessary to decode the information
# read JSON
info_api = json.loads(data)  # loads(). is a method from JSON library (read JSON response)

# Obtain information . We use 'seq' and 'desc' as keys
sequence = info_api['seq']
description = info_api['desc']

# PRINTING
tc.cprint("Gene: ", 'green', end="")
print(gene)

tc.cprint("Description: ", 'green', end="")
print(description)

tc.cprint("Bases: ", 'green', end="")
print(sequence)
