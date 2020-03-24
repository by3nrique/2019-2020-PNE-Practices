import http.server
import socketserver
import termcolor
from pathlib import Path

# Define the Server's port
PORT = 8080

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

        body = """
        <!DOCTYPE html>
        <html lang="en" dir="ltr">
          <head>
            <meta charset="utf-8">
            <title>RESULT</title>
          </head>
          <body>
            <h2>Echoing the received message:</h2>
            <p></p>
            <a href="http://127.0.0.1:8080/">Main Page </a>
          </body>
        </html>
        """

        if self.path == "/":

            file = "form-EX02.html"

            contents = Path(file).read_text()

            self.send_response(200)  # -- Status line: OK!

        elif "/echo" == self.path[0:5]:

            chk = self.path[self.path.find("chk") + 4:]

            if "chk" in self.path and "on" == chk:
                msg = self.path[self.path.find("msg") + 4: self.path.find("&")]
                msg_converted = msg.upper()

            else:
                msg = self.path[self.path.find("msg") + 4:]
                msg_converted = msg

            contents = body[0:body.find("<p>") + 3] + msg_converted + body[body.find("</p>"):]
            self.send_response(200)  # -- Status line: OK!

        else:
            file = "Error.html"
            contents = Path(file).read_text()
            self.send_response(404)  # -- Status line: ERROR NOT FOUND

        # Generating the response message
        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

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
