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

server = 'rest.ensembl.org'
endpoint = '/sequence/id/'
options = GENES[gene] + '?content-type=application/json'
method = "GET"
URL = server + endpoint + options

print(f"\nConnecting to server: {server}")
print(f"URL : {URL}")

# Connect the server
connection = http.client.HTTPConnection(server)

try:
    connection.request(method, endpoint + options)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# response and status
response = connection.getresponse()
print(f"Response received!: {response.status} {response.reason}\n")

data = response.read().decode("utf-8")
# read JSON
info_api = json.loads(data)

# Obtain information
sequence = info_api['seq']
description = info_api['desc']

# PRINTING
tc.cprint("Gene: ", 'green', end="")
print(gene)

tc.cprint("Description: ", 'green', end="")
print(description)

tc.cprint("Bases: ", 'green', end="")
print(sequence)
