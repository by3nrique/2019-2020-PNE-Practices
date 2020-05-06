# Import the necessary
from Seq1 import Seq
import socket
import termcolor

# IP and PORT
PORT = 8080
IP = "127.0.0.1"

# This is list with example sequences

seq_list = ["TGTGAACATTCTGCACAGGTCTCTGGCTGCGCCTGGGCGGGTTTCTT", "CAGGAGGGGACTGTCTGTGTTCTCCCTCCCTCCGAGCTCCAGCCTTC",
            "CTCCCAGCTCCCTGGAGTCTCTCACGTAGAATGTCCTCTCCACCCC", "GAACTCCTGCAGGTTCTGCAGGCCACGGCTGGCCCCCCTCGAAAGT",
            "CTGCAGGGGGACGCTTGAAAGTTGCTGGAGGAGCCGGGGGGAA"]

# Server
# Listening socket
lsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Preventing the error: "Port already in use"
lsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

lsocket.bind((IP, PORT))  # Socket's IP and PORT with .bind() method

# -- Become a listening socket
lsocket.listen()

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
        # Receive the message
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()

        try:
            msg_info = msg.split(" ")  # split the msg "GET 1" into ["GET","1"]
            service = msg_info[0]  # For example GET
            argument = msg_info[1]  # 1 , 2

        except IndexError:
            service = msg

        # PING command
        if "PING" == service:
            response = "OK!\n"  # Return response OK!!

        # GET command
        elif "GET" == service:
            response = seq_list[int(argument)]

        # INFO command
        elif "INFO" == service:
            seq_info = Seq(argument)  # argument is the sequence
            count_bases_string = ""

            for base, count in seq_info.count().items():
                s_base = str(base) + ": " + str(count) + " (" + str(
                    round(count / seq_info.len() * 100, 2)) + "%)" + "\n"
                count_bases_string += s_base

            response = ("Sequence: " + str(seq_info) + "\n" +
                        "Total length: " + str(seq_info.len()) + "\n" +
                        count_bases_string)

        elif "COMP" == service:
            seq_comp = Seq(argument)
            response = seq_comp.complement() + "\n"

        elif "REV" == service:
            seq_rev = Seq(argument)
            response = seq_rev.reverse() + "\n"

        elif "GENE" == service:
            gene = argument
            s = Seq()
            s.read_fasta("../Session-04/" + gene + ".txt")
            response = str(s) + "\n"

        # Server Console

        termcolor.cprint(f'{service} command!', "green")
        print(response)

        # Client console

        cs.send(response.encode())  # Encode the message and send message
        # Close
        cs.close()
