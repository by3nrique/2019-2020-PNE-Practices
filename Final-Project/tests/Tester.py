import http.client
import termcolor

print('-----|Final Project Test report|------')

# -- Parameters
IP = 'localhost'
PORT = 8080

# Details of the connection
print(f'Connection to SERVER at {IP}:{PORT}')

list_test_basic = ['http://localhost:8080/listSpecies', 'http://localhost:8080/listSpecies?limit=10',
                   'http://localhost:8080/listSpecies?limit=100',
                   'http://localhost:8080/karyotype?specie=mouse', 'http://localhost:8080/karyotype?specie=human',
                   'http://localhost:8080/chromosomeLength?specie=mouse&chromo=18',
                   'http://localhost:8080/chromosomeLength?specie=enrique&chromo=X',
                   'http://localhost:8080/listSpecies?limit=URJC',
                   'http://localhost:8080/karyotype?specie=cat', 'http://localhost:8080/karyotype?specie=dog',
                   'http://localhost:8080/chromosomeLength?specie=enrique&chromo=18',
                   'http://localhost:8080/chromosomeLength?specie=cat&chromo=X']

list_test_medium = ['http://localhost:8080/geneSeq?gene=FRAT1',
                    'http://localhost:8080/geneSeq?gene=URJC1',
                    'http://localhost:8080/geneSeq?gene=GNG5', 'http://localhost:8080/geneInfo?gene=GNG5',
                    'http://localhost:8080/geneInfo?gene=URJC1', 'http://localhost:8080/geneCalc?gene=URJC11',
                    'http://localhost:8080/geneInfo?gene=FRAT1', 'http://localhost:8080/geneCalc?gene=FRAT1',
                    'http://localhost:8080/geneCalc?gene=GNG5',
                    'http://localhost:8080/geneList?chromo=1&start=0&end=30000',
                    'http://localhost:8080/geneList?chromo=1&start=29990&end=30000',
                    'http://localhost:8080/geneList?chromo=4&start=0&end=30000'] + list_test_basic

# Create the JSON requests
list_json = []
for r in list_test_medium:
    list_json.append(r + '&json=1')
list_test_advanced = list_test_medium + list_json


def write_file(all_data, new_filename):
    with open(new_filename, 'w') as f:
        f.write(all_data)  # Writes in the new_file
    f.close()
    termcolor.cprint('Test report --> ' + new_filename, 'green')


def test_maker(test_list, ip, port):
    client = http.client.HTTPConnection(ip, port)
    string_file = 'Test report\n============\n'
    index = 0
    for test in test_list:
        index += 1

        request = test.replace('http://localhost:8080', '')
        client.request('GET', request)
        response = client.getresponse()
        read_response = response.read().decode(encoding='utf-8')

        termcolor.cprint(f'Performing TEST {index}', 'blue')
        termcolor.cprint(test, 'green')

        string_file += f'* TEST: {test_list.index(test)}\n'
        string_file += f'* Input: {test}\n'
        string_file += f'* Output: {read_response}\n'

    return string_file


# TEST BASIC
data_test_basic = test_maker(list_test_basic, IP, PORT)
write_file(data_test_basic, 'test_basic.txt')

# TEST MEDIUM
data_test_medium = test_maker(list_test_medium, IP, PORT)
write_file(data_test_medium, 'test_medium.txt')

# TEST MEDIUM
data_test_advanced = test_maker(list_test_advanced, IP, PORT)
write_file(data_test_advanced, 'test_advanced.txt')

