# Import the libaries
import pathlib
import socket
import termcolor

# Server Information
IP = "127.0.0.1"
PORT = 8080


def read(FILENAME):  # read() is the function read_fasta_data() from other practice
    # open and read the file
    file_contents = pathlib.Path(FILENAME).read_text().split("\n")[1:]  # Split lines and skip the first one [1:]
    body = "".join(file_contents)  # Join all the list in the same string without spaces
    return body


def process_client(s):
    # Receive the message
    req_raw = s.recv(2000)
    request_received = req_raw.decode()

    print("Message from CLIENT: ")

    lines = request_received.split('\n')  # Split the request
    first_line = lines[0]  # first LINE of the request

    print("Request line: ", end=" ")
    termcolor.cprint(first_line, "green")

    # Response message
    FOLDER = "../P4/"

    file_request = first_line.split(" ")[1]
    # file_request is like req_line (GET /info/A HTTP/1.1) only with (/info/A) or  (/info/C)

    if "/info/A" == file_request:
        FILENAME = "A.html"
        body = read(FOLDER + FILENAME)  # read() is the function read_fasta_data() from other practice
    elif "/info/C" == file_request:
        FILENAME = "C.html"
        body = read(FOLDER + FILENAME)
    else:
        body = ""

    # This new contents are written in HTML language
    # Status line
    status_line = "HTTP/1.1 200 OK\n"  # everything is ok (200 code)

    # Content-Type header and Content-Length
    header = "Content-Type: text/html\n"
    header += f"Content-Length: {len(body)}\n"

    # Join all the parts
    response = status_line + header + "\n" + body  # Join the status_line , header and body
    cs.send(response.encode())  # send the response


# Server
# Listening socket
lsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Preventing the error: "Port already in use"
lsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

lsocket.bind((IP, PORT))  # Socket's IP and PORT with .bind() method

# -- Become a listening socket
lsocket.listen()

print("SEQ Server configured!")

# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = lsocket.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        lsocket.close()
        exit()
    else:

        # Service the client
        process_client(cs)  # This is the function created above

        # Close
        cs.close()
