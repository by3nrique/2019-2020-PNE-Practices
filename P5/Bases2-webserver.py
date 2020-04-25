# Import libraries
import http.server
import pathlib
import socketserver
import termcolor

# PORT
PORT = 8080

# Preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


def read_file(FILENAME):  # read_file() is the function read_fasta_data() from other practice
    # open and read the file
    file_contents = pathlib.Path(FILENAME).read_text().split("\n")[1:]  # Split lines and skip the first one [1:]
    body = "".join(file_contents)  # Join all the list in the same string without spaces
    return body


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler (another class)
# class inheritates all its methods
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # ----------------------------------------------------------------------------------
        # Modifications for Practice 5

        # Message to send back to the client:
        FOLDER = "../P5/"
        if self.path == "/" or self.path == "/index.html":  # self.path is the path of the request
            file = "index.html"
            # Generating the response message
        else:  # example /info/A.html
            file = self.path

        try:
            contents = read_file(FOLDER + file)  # read_file() is the function read_fasta_data() from other practice
            # Generating the response message
            self.send_response(200)  # -- Status line: OK!
        except FileNotFoundError:
            contents = read_file(FOLDER + "Error.html")
            # Generating the response message
            self.send_response(404)  # -- Status line: ERROR NOT FOUND

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')  # Changed form text\plain to text text\html
        self.send_header('Content-Length', str(len(contents.encode())))

        # ----------------------------------------------------------------------------------

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# - Server program
Handler = TestHandler  # User our handler

# create socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:  # If we want to close the server we use KeyboardInterrupt exception
        print("")
        print("Stoped by the user")
        httpd.server_close()
