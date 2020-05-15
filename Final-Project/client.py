from api import ApiConnector
import termcolor

# Connection settings
PORT = 8080
SERVER = 'localhost'


# Print the JSON4 data received

def print_dict(data, nesting=-5):
    if type(data) == dict:
        print('')
        nesting += 5
        for d in data:
            print(nesting * ' ', end='')
            print(d, end=': ')
            print_dict(data[d], nesting)
    else:
        termcolor.cprint(data, 'blue')


# Menu
def show_menu():
    print("\n\t1 - /listSpecies (limit)")
    print("\t2 - /karyotype ")
    print("\t3 - /chromosomeLength")
    print("\t4 - /geneSeq")
    print("\t5 - /geneInfo")
    print("\t6 - /geneCalc")
    print("\t7 - /geneList")
    print("\t8 - Exit")


menu = True
while menu:
    show_menu()
    choose_option = int(input('Choose an option from the menu: '))
    if choose_option == 1:
        # Choose the limit parameter
        limit_parameter = input('Number of species to show [optional]: ')

        # Information for the request
        client_request = '/listSpecies?limit=' + limit_parameter

        # Create the connection with the server
        connection = ApiConnector(endpoint=client_request, server=f'{SERVER}:{PORT}')
        response_api, error_code = connection.api_response()

        # Print the information received
        termcolor.cprint('\nInformation received', 'blue')

        # Print the information received
        print_dict(response_api)

    elif choose_option == 2:
        # Choose the limit parameter
        specie_parameter = input("Choose specie: ")

        # Information for the request
        client_request = '/karyotype?specie=' + specie_parameter

        # Create the connection with the server
        connection = ApiConnector(endpoint=client_request, server=f'{SERVER}:{PORT}')
        response_api, error_code = connection.api_response()

        # Print the information received
        termcolor.cprint('\nInformation received', 'blue')
        print_dict(response_api)

    elif choose_option == 3:
        # Choose the limit parameter
        specie_parameter = input('Choose specie: ')
        chr_parameter = input('Choose chromosome: ')

        # Information for the request
        client_request = f'/chromosomeLength?specie={specie_parameter}&chromo={chr_parameter}'

        # Create the connection with the server
        connection = ApiConnector(endpoint=client_request, server=f'{SERVER}:{PORT}')
        response_api, error_code = connection.api_response()

        # Print the information received
        termcolor.cprint('\nInformation received', 'blue')
        print_dict(response_api)

    elif choose_option == 4:
        # Choose the limit parameter
        gene_parameter = input('Choose a human gene: ')

        # Information for the request
        client_request = '/geneSeq?gene=' + gene_parameter

        # Create the connection with the server
        connection = ApiConnector(endpoint=client_request, server=f'{SERVER}:{PORT}')
        response_api, error_code = connection.api_response()

        # Print the information received
        termcolor.cprint('\nInformation received', 'blue')
        print_dict(response_api)

    elif choose_option == 5:
        # Choose the limit parameter
        gene_parameter = input('Choose a human gene: ')

        # Information for the request
        client_request = '/geneInfo?gene=' + gene_parameter

        # Create the connection with the server
        connection = ApiConnector(endpoint=client_request, server=f'{SERVER}:{PORT}')
        response_api, error_code = connection.api_response()

        # Print the information received
        termcolor.cprint('\nInformation received', 'blue')
        print_dict(response_api)

    elif choose_option == 6:
        # Choose the limit parameter
        gene_parameter = input('Choose a human gene: ')

        # Information for the request
        client_request = '/geneCalc?gene=' + gene_parameter

        # Create the connection with the server
        connection = ApiConnector(endpoint=client_request, server=f'{SERVER}:{PORT}')
        response_api, error_code = connection.api_response()

        # Print the information received
        termcolor.cprint('\nInformation received', 'blue')
        print_dict(response_api)

    elif choose_option == 7:
        # Choose the limit parameter
        chr_parameter = input('Choose a human chromosome: ')
        start_parameter = input('Choose the start point: ')
        end_parameter = input('Choose the end point: ')

        # Information for the request
        client_request = f'/geneList?chromo={chr_parameter}&start={start_parameter}&end={end_parameter}'

        # Create the connection with the server
        connection = ApiConnector(endpoint=client_request, server=f'{SERVER}:{PORT}')
        response_api, error_code = connection.api_response()

        # Print the information received
        termcolor.cprint('\nInformation received', 'blue')
        print_dict(response_api)

    elif choose_option == 8:
        menu = False
    else:
        print('Choose a valid option(1-6) or exit(7) the client')
