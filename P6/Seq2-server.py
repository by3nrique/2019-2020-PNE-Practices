import http.server
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq

# Define the Server's port
PORT = 8080


def html_response(title="", body=""):  # Generate HTML response with JUST  title and body
    default_body = f"""
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>{title}</title>
  </head>
  <body>{body}
    </body>
    <body>
    <a href="http://127.0.0.1:8080/">Main Page </a>
  </body>
</html>
"""

    return default_body


def argument_command(request_line):
    argument = request_line[request_line.find("=") + 1:]
    return argument


def analyze_request(request_line):
    if "?" in request_line:  # Analyse if the request is simple or with parameters

        request_parts = request_line.split("?")  # Divide de request into endpoint and parameter/s

        endpoint = request_parts[0]  # /ping

    else:  # Simple request (no parameters) http:/localhost:8080/
        endpoint = request_line

    # return endpoint , parameters and the JSON option
    return endpoint


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        endpoint = analyze_request(self.path)
        if endpoint == "/":

            file = "form-4.html"

            contents = Path(file).read_text()

            error = 200

        elif "/ping" == endpoint:
            html = "<h1>PING OK!</h1><p>The SEQ2 server is running...</p>"
            contents = html_response("PING", html)
            error = 200

        elif "/get" == endpoint:

            seq_list = ["TGTGAACATTCTGCACAGGTCTCTGGCTGCGCCTGGGCGGGTTTCTT",
                        "CAGGAGGGGACTGTCTGTGTTCTCCCTCCCTCCGAGCTCCAGCCTTC",
                        "CTCCCAGCTCCCTGGAGTCTCTCACGTAGAATGTCCTCTCCACCCC",
                        "GAACTCCTGCAGGTTCTGCAGGCCACGGCTGGCCCCCCTCGAAAGT",
                        "CTGCAGGGGGACGCTTGAAAGTTGCTGGAGGAGCCGGGGGGAA"]

            sequence_number = int(argument_command(self.path))
            sequence = seq_list[sequence_number]

            html = "<h1>Sequence number " + str(sequence_number) + "</h1><p>" + sequence + "</p>"
            contents = html_response("GET", html)

            error = 200  # -- Status line: OK!

        elif "/gene" == endpoint:

            gene = argument_command(self.path)

            s = Seq()
            s.read_fasta("../Session-04/" + gene + ".txt")

            html = "<h1>Gene Sequence: " + gene + '</h1><textarea readonly rows = "20" cols = "80">' + str(
                s) + '</textarea>'
            contents = html_response("GENE", html)

            error = 200

        elif "/operation" == endpoint:

            requests = self.path.split("&")
            sequence = argument_command(requests[0])
            operation = argument_command(requests[1])

            user_seq = Seq(sequence)
            if ("ERROR" or "NULL") in str(user_seq):
                operation = ""
                html_operation = "<h1>Operation:</h1>"
                html_result = "<h1>Result:</h1>" + "<p>The sequence is not valid</p>"
            if "info" == operation:
                count_bases_string = ""
                for base, count in user_seq.count().items():
                    s_base = str(base) + ": " + str(count) + " (" + str(
                        round(count / user_seq.len() * 100, 2)) + "%)" + "<br>"
                    count_bases_string += s_base

                response_info = ("Sequence: " + str(user_seq) + " <br>" +
                                 "Total length: " + str(user_seq.len()) + "<br>" +
                                 count_bases_string)

                html_operation = "<h1>Operation:</h1><p>Info</p>"
                html_result = "<h1>Result:</h1>" + "<p>" + response_info + "</p>"

            elif "comp" == operation:
                response_comp = user_seq.complement() + "\n"

                html_operation = "<h1>Operation:</h1><p>Comp</p>"
                html_result = "<h1>Result:</h1>" + "<p>" + response_comp + "</p>"

            elif "rev" == operation:
                response_rev = user_seq.reverse() + "\n"

                html_operation = "<h1>Operation:</h1><p>Rev</p>"
                html_result = "<h1>Result:</h1>" + "<p>" + response_rev + "</p>"

            html_sequence = "<h1>Sequence:</h1>" + "<p>" + sequence + "</p>"
            html = html_sequence + html_operation + html_result

            contents = html_response("OPERATION", html)
            error = 200

        else:
            file = "Error.html"
            contents = Path(file).read_text()
            error = 404  # -- Status line: ERROR NOT FOUND

        self.send_response(error)
        # Generating the response message
        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(str.encode(contents))))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(str(contents)))

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
        print("Stoped by the user")
        httpd.server_close()
