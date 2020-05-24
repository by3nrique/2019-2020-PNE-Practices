import http.server
import socketserver
import termcolor
from pathlib import Path
import json
from api import ApiConnector
from Seq1 import Seq

# Server configuration
HTML = '../Final-Project/html/'
PORT = 8080


def html_response(title="", body="", error=False):
    if error:
        color = "#f26b5b"  # Red color
    else:
        color = "whitesmoke"

    contents_css = Path(HTML + 'style.css').read_text()
    # For the html responses we use this template , this function replaces the title and body of the template
    default_body = f'''
        <!DOCTYPE html>
        <html lang="en" dir="ltr">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
            <title>{title}</title>
            <style>{contents_css}</style>
          </head>
          <body>
            <div style="background-color: {color};"id="wrapper">
              <h1>Browsing Human and vertebrates genome</h1>
              <h2>Results : {title}</h2>
              <p>{body}</p>
              <a style="float:left;" href="/1"><h3>BASIC SERVICES</h2></a><a style="float:right;"href="/2"><h3>MEDIUM 
SERVICES</h2></a> 
            </div>
          </body>
        </html>
        '''
    return default_body


def analyze_request(request_line):
    # example with http://localhost:8080/chromosomeLength?specie=mouse&chromo=18

    JSON = False  # By default if not indicated the request is not a JSON request

    if "?" in request_line:  # Analyse if the request is simple or with parameters

        request_parts = request_line.split("?")  # Divide de request into endpoint and parameter/s

        endpoint = request_parts[0]  # /chromosomeLength

        try:  # try if the are multiple parameters with split method

            all_parameters_request = request_parts[1].split("&")

        except ValueError:  # If there is one parameter we don't need to split

            all_parameters_request = request_parts[1]

        # Create a list of tuples ... [("specie","mouse"),("chromo",18)]
        list_parameters = []
        for parameter_request in all_parameters_request:
            (parameter_name, value) = parameter_request.split("=")  # Split parameter and value for it
            list_parameters.append((parameter_name, value))  # append ("specie","mouse") and ("chromo",18)

        if ('&' and 'json=1') in request_line:  # Analyze if it is json request (Advanced service)
            JSON = True

    else:  # Simple request (no parameters) http:/localhost:8080/
        if ('&' and 'json=1') in request_line:  # Analyze if it is json request (Advanced service)
            endpoint = request_line.split("&")[0]
            list_parameters = []
            JSON = True
        else:
            endpoint = request_line
            list_parameters = []



    # return endpoint , parameters and the JSON option
    return endpoint, list_parameters, JSON


def geneID_lookup(gene):  # This functions looks for the GENE ID
    # Connection  with Enssembl (Obtain id)
    # ApiConnector is explained in api.py
    connection = ApiConnector('/xrefs/symbol/homo_sapiens/' + gene)
    connection_response, status = connection.api_response()
    # Results of connection
    if status == 200:
        id_gene = connection_response[0]['id']  # This is the ID of the gene
        response = {'id': f'{id_gene}'}
    else:  # If the status is not 200 , we create an "error response"
        response = {'error': f'Gene {gene} not found'}
    return response, status


def response_error(title, body):
    # This function generates all the information for an error response (HTML ,JSON and Error code)x
    # HTML RESPONSE
    contents_html = html_response(title, body, error=True)
    # JSON RESPONSE
    contents_json = json.dumps({'Error': f'{body}'})
    error_code = 400  # Generic Error
    return contents_html, contents_json, error_code


def sequence_information(sequence):
    # See Seq1.py for information about the class Seq
    seq_info = Seq(sequence)
    length_sequence = seq_info.len()
    bases_information = {}  # This is a dictionary with the count a percentage for each base

    # Bases_information = [(A,817,25),(T,928,40)....]
    for base, count in seq_info.count().items():
        # .items() returns the base and the count for each base
        percentage = round(count / seq_info.len() * 100, 2)

        keys = ['Count', 'Fraction']
        base_count = count
        base_percentage = f'{percentage}%'

        dict_base = dict(zip(keys, [base_count, base_percentage]))  # Dictionary with information of a base
        dict_bases = {base: dict_base}  # Dictionary with the information of all the bases

        bases_information.update(dict_bases)

    return length_sequence, bases_information


def sequence_information_html(sequence):
    seq_info = Seq(sequence)
    count_bases_string = ""
    for base, count in seq_info.count().items():
        percentage = round(count / seq_info.len() * 100, 2)
        s_base = f'{base}: {count} ({percentage}%)</br>'
        count_bases_string += s_base

    reponse_info = (f'<textarea readonly rows = "20" cols = "80">{seq_info}</textarea>' + " <br>" +
                    "Total length: " + str(seq_info.len()) + "<br>" +
                    count_bases_string)
    return reponse_info


# error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler.
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # Print the request line
        termcolor.cprint('\n' + self.requestline, 'green')
        endpoint, parameters_info, JSON = analyze_request(self.path)  # Process the request

        # Create the variables used
        contents_json = ""
        contents_html = ""
        error_code = ""
        response_api = ""

        try:
            # admitted endpoints
            # /listSpecies /karyotype /chromosomeLength /geneSeq /geneInfo /geneCalc /geneList

            if endpoint == '/' or endpoint == '/1':
                if JSON:
                    contents_html, contents_json, error_code = response_error('Error',
                                                                              f'JSON not valid in this endpoint "{endpoint}"')
                else:
                    file = HTML + '1.html'  # 1.html is the form for BASIC services
                    contents_html = Path(file).read_text()  # Read the file
                    error_code = 200  # OK !


            elif endpoint == '/2':
                if JSON:
                    contents_html, contents_json, error_code = response_error('Error',
                                                                              f'JSON not valid in this endpoint "{endpoint}"')
                else:
                    file = HTML + '2.html'  # 1.html is the form for BASIC services
                    contents_html = Path(file).read_text()  # Read the file
                    error_code = 200  # OK !

            elif endpoint == '/listSpecies':
                # Connection with Enssembl
                # ApiConnector is explained in api.py
                connection = ApiConnector('/info/species')
                response_api, error_code = connection.api_response()

                # Parameters of the request
                try:
                    user_limit = int(parameters_info[0][1])  # User_limit = Number of species to show

                except (IndexError, ValueError):
                    # If there is an IndexError or ValueError parameters_info[0][1] we dont consider the parameters
                    user_limit = len(response_api['species'])  # User_limit = Number of species to show

                # Generate response
                # JSON response:
                if JSON:
                    species_dict = {}
                    index = 0
                    for specie in response_api['species'][:user_limit]:
                        index += 1
                        # 'specie' is the key that returns a list of the species
                        # Create a list with all the species
                        species_dict.update({index: specie['display_name']})

                    # We create a dictionary for the response
                    datastore = {'Species': species_dict}
                    contents_json = json.dumps(datastore)

                # html Response
                else:
                    species_html = ""
                    for specie in response_api['species'][0:user_limit]:
                        # 'specie' is the key that returns a list of the species
                        # Create html with the <li></li> tags (·specie) for every specie
                        species_html += f'<li>{specie["display_name"]}</li>'
                    contents_html = html_response(f'List of {user_limit} species',
                                                  f'''<div style="height:350px;padding-left:12px;overflow:auto;">
                                                            <lu>{species_html}</lu>
                                                        </div>''')
                    # html_response() creates a html response using a template

            elif endpoint == '/karyotype':
                # Parameters of the request
                specie = parameters_info[0][1]

                # Connection with Enssembl
                connection = ApiConnector('/info/assembly/' + specie)
                response_api, error_code = connection.api_response()

                # Generate response
                karyotype_html = ""
                karyotype_list = []
                for chromosome in response_api['karyotype']:
                    karyotype_html += f"""<li>{chromosome}</li>"""
                    karyotype_list.append(chromosome)

                # JSON response
                if JSON:
                    datastore = {'Specie': {specie: {'Karyotype': response_api['karyotype']}}}
                    contents_json = json.dumps(datastore)

                # HTML response
                else:
                    contents_html = html_response(f'Karyotype {specie}', f'''<div style="height:350px;padding-left
:12px;overflow:auto;"> 
                                                            <lu>{karyotype_html}</lu>
                                                        </div>''')

            elif endpoint == "/chromosomeLength":
                # Parameters of the request
                specie = parameters_info[0][1]
                chromosome = parameters_info[1][1]

                # Connection with Enssembl
                connection = ApiConnector('/info/assembly/', arguments=f'{specie}/{chromosome}')
                response_api, error_code = connection.api_response()

                # Generate response
                chromosome_length = response_api['length']

                # JSON response
                if JSON:
                    datastore = {'Specie': {specie: {'Chromosome': {chromosome: {'Length': chromosome_length}}}}}
                    contents_json = json.dumps(datastore)

                # HTML Response
                else:
                    chromosome_information_html = f"""
                                            <br>Specie: {specie}</br>
                                            <br>Chromosome: {chromosome}</br>
                                            <br>Length: {chromosome_length}</br>
                                        """
                    contents_html = html_response(f"Chromosome length", chromosome_information_html)

            elif endpoint == "/geneSeq":
                # Parameters of the request
                gene = parameters_info[0][1]

                # Quick lookup for the ID
                response_api, error_code = geneID_lookup(gene)  # This is the ID of the gene
                gene_id = response_api['id']

                # Connection 2 with Enssembl (Obtain Sequence)
                connection_2 = ApiConnector('/sequence/id/' + gene_id)
                response_api, error_code = connection_2.api_response()

                # Results of connection 2
                sequence = response_api['seq']

                # Generate response

                # JSON response
                if JSON:
                    datastore = {'Gene': {gene: {'Gene id': gene_id, 'Sequence': sequence}}}
                    contents_json = json.dumps(datastore)

                # html response
                else:
                    contents_html = html_response('Gene sequence',
                                                  f'<textarea readonly rows = "20" cols = "80">{sequence}'
                                                  f'</textarea>')

            elif endpoint == '/geneInfo':
                # Parameters of the request
                gene = parameters_info[0][1]

                # Quick lookup for the ID
                response_api, error_code = geneID_lookup(gene)  # This is the ID of the gene
                gene_id = response_api['id']

                # Connection 2 with Enssembl
                connection_2 = ApiConnector('/lookup/id/' + gene_id)
                response_api, error_code = connection_2.api_response()

                # Results of connection 2
                gene_start = response_api['start']
                gene_end = response_api['end']
                gene_length = int(gene_end) - int(gene_start) + 1  # We calculate the gene length
                gene_location = response_api['seq_region_name']

                # Generate response

                # JSON response
                if JSON:
                    datastore = {'Gene': {
                        gene: {'Gene id': gene_id, 'Chromosome': gene_location, 'Length': gene_length,
                               'Start': gene_start, 'End': gene_end}}}
                    contents_json = json.dumps(datastore)

                # HTML response
                else:
                    gene_information_html = f"""
                        <br>Gene id: {gene_id}</br>
                        <br>Length: {gene_length}</br>
                        <br>Start: {gene_start}</br>
                        <br>End: {gene_end}</br>
                        <br>Chromosome: {gene_location}</br>
                    """
                    contents_html = html_response('Gene information', gene_information_html)

            elif endpoint == '/geneCalc':
                # Parameters of the request
                gene = parameters_info[0][1]

                # Quick lookup for the ID
                response_api, error_code = geneID_lookup(gene)  # This is the ID of the gene
                gene_id = response_api['id']

                # Connection 2 with Enssembl (Obtain Sequence)
                connection_2 = ApiConnector('/sequence/id/' + gene_id)
                response_api, error_code = connection_2.api_response()

                # Results of connection 2
                sequence = response_api['seq']

                # Generate response
                length, dict_bases = sequence_information(sequence)

                # JSON response
                if JSON:
                    datastore = {'Gene': {gene: {'Gene id': gene_id,
                                                 'Length': length, 'Bases': dict_bases}}}
                    contents_json = json.dumps(datastore)

                # HTML response
                else:
                    calc_html = sequence_information_html(sequence)
                    contents_html = html_response("Sequence information", calc_html)

            elif endpoint == '/geneList':
                # Parameters of the request

                chromosome = parameters_info[0][1]
                start = parameters_info[1][1]
                end = parameters_info[2][1]

                # Connection with Enssembl
                connection = ApiConnector('/overlap/region/human/', arguments=f'{chromosome}:{start}-{end}',
                                          feature=";feature=gene")
                response_api, error_code = connection.api_response()

                # Generate response
                geneList = []
                geneList_html = ''
                for gene in response_api:
                    geneList_html += f"""<br>{gene['external_name']}</br>"""
                    geneList.append(gene['external_name'])

                # JSON response
                if JSON:
                    datastore = {'Specie': {
                        'Homo sapiens': {'Chromosome': {chromosome: {f'Region{start}:{end}': geneList}}}}}
                    contents_json = json.dumps(datastore)

                # HTML response
                else:
                    genes_information_html = f"""<div style="height:350px;padding-left:12px;overflow:auto;">
                                                            <lu>{geneList_html}</lu>
                                                        </div>"""
                    contents_html = html_response("Gene list", genes_information_html)

            # -------- ERROR PROCESSING ----------------------------------------------

            else:  # Errors while choosing an endpoint
                contents_html, contents_json, error_code = response_error('Error', 'Choose a valid endpoint')

        except (KeyError, TypeError):  # Errors while processing the response
            try:  # Automatic generated error
                error_generated = response_api['error']
            except (KeyError, TypeError):
                if error_code == 400:  # Bad connection with the enssemble server
                    error_generated = 'Bad request'
                elif error_code == 204:  # Empty response
                    error_generated = 'Empty response'
                else:  # Other error
                    error_generated = 'Unknown error , try again'

            # Generate de errors response
            contents_html, contents_json, error_code = response_error('Error', error_generated)

        except IndexError:  # Index Error are generated from extracting the parameters from the request
            contents_html, contents_json, error_code = response_error('Error', 'Not enough parameters in the request')

        # Generating the html response message
        self.send_response(error_code)
        if JSON:
            contents = contents_json
            # Define the content-type header:
            self.send_header('Content-Type', 'text/plain')

        else:
            contents = contents_html
            # Define the content-type header:
            self.send_header('Content-Type', 'text/html')

        self.send_header('Content-Length', str(len(str.encode(contents))))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return

    def log_message(self, formatn, *args):  # Not automatic http log in the terminal
        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
