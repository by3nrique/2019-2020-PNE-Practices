# Import the required libraries
import http.client
import json
import termcolor as tc

server = 'rest.ensembl.org'  # Server address
endpoint = '/info/ping'  # This endpoint returns OK!
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
# .getresponse() method that returns the reponse information from the server

tc.cprint(f"Response received!: {response.status} {response.reason}\n", 'blue')

data = response.read().decode("utf-8")  # It is necessary to decode the information
# read JSON
info_api = json.loads(data)  # loads(). is a method from JSON library  (read JSON response)

# PING
ping = info_api['ping']  # OK!

if ping == 1:  # if the response is == 1 the server is OK!
    print("PING OK! The database is running!")
