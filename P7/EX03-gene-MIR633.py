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
params = GENES[gene] + '?content-type=application/json'
method = "GET"
URL = server + endpoint + params

print(f"\nConnecting to server: {server}")
print(f"URL : {URL}")

# Connect with the server
conn = http.client.HTTPConnection(server)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request(method, endpoint + params)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
info_api = json.loads(data1)

# Obtain the information from the JSON file
sequence = info_api['seq']
description = info_api['desc']

# PING
tc.cprint("Gene: ", 'green', end="")
print(gene)

tc.cprint("Description: ", 'green', end="")
print(description)

tc.cprint("Bases: ", 'green' , end="")
print(sequence)
