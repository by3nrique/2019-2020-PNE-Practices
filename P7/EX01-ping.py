import http.client
import json

server = 'rest.ensembl.org'
endpoint = '/info/ping'
options = '?content-type=application/json'
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

# PING
ping = info_api['ping']

if ping == 1:  # if the response is == 1 the server is OK!
    print("PING OK! The database is running!")
