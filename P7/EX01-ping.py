import http.client
import json

server = 'rest.ensembl.org'
endpoint = '/info/ping'
params = '?content-type=application/json'
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

# PING
ping = info_api['ping']

if ping == 1:  # if the response is == 1 the server is OK!
    print("PING OK! The database is running!")
