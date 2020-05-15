import http.client
import termcolor
import json


class ApiConnector:
    """A class to handle conections with essemble api"""

    def __init__(self, endpoint, server='rest.ensembl.org', arguments="", feature=""):

        self.server = server  # Define the server
        self.method = 'GET'  # Default method
        self.endpoint = endpoint

        if self.server == 'rest.ensembl.org':  # Request to ensembl server

            self.arguments = arguments + '?content-type=application/json' + feature  #
        else:
            self.arguments = arguments + '&json=1'  # (Advanced Option) This is for requests to Server.py

        URL = self.server + self.endpoint + self.arguments

        # The URL is like rest.ensembl.org/info/assembly/mouse/18?content-type=application/json

        # Print information about the connection

        termcolor.cprint('\n------- Query to server -------', 'blue')
        termcolor.cprint(f'Connection to server: {self.server}', 'blue')
        termcolor.cprint(f'URL : {URL}', 'blue')

    def api_response(self, ):  # this function connects and gets the response
        connection = http.client.HTTPConnection(self.server)

        try:
            connection.request(self.method, self.endpoint + self.arguments)

        except ConnectionRefusedError:
            termcolor.cprint("ERROR! Cannot connect to the Server", "red")
            exit()

        # response and status
        initial_response = connection.getresponse()

        # Process the server's response

        json_response = initial_response.read().decode("utf-8")  # Data in json format
        final_response = json.loads(json_response)  # Read the JSON file

        # Different colors for the response codes 200 OK!= green ; other = red
        if len(final_response) == 0:  # if the response is empty we consider that it is an error
            color_response = 'red'
            final_response = [['Error']]
            error_code = 204  # Empty response
        else:
            error_code = initial_response.status
            if error_code == 200:
                color_response = 'green'
            else:
                color_response = 'red'

        termcolor.cprint(f"Response received!: {error_code}\n", color_response)

        return final_response, error_code
