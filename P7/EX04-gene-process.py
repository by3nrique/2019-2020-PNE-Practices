import http.client
import json
import termcolor as tc
from Seq1 import Seq


def sequence_information(bases):
    seq_info = Seq(bases)
    min_count = 0
    most_frecuent_base = ""

    tc.cprint("Total length:", 'green', end=' ')
    print(seq_info.len())

    for base, count in seq_info.count().items():
        # .items() returns the base and the count for each base , then we print
        percentage = round(count / seq_info.len() * 100, 2)
        tc.cprint(f"{base}:", 'blue', end=' ')
        print(f" {count} ({percentage}%)")

        # here we look for the most frecuent base
        if min_count < count:
            min_count = count
            most_frecuent_base = base

    # print the most frecuent base
    tc.cprint("Most frecuent Base:", 'green', end=' ')
    print(most_frecuent_base)


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

gene = input('Write the gene name:')

server = 'rest.ensembl.org'
endpoint = '/sequence/id/'
options = GENES[gene] + '?content-type=application/json'
method = "GET"
URL = server + endpoint + options

print(f"\nConnecting to server: {server}")
print(f"URL : {URL}")

# Connect w the server
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

# information

sequence = (info_api['seq'])
description = info_api['desc']

# RESULTS
tc.cprint("Gene: ", 'green', end="")
print(gene)

tc.cprint("Description: ", 'green', end="")
print(description)

sequence_information(sequence)
