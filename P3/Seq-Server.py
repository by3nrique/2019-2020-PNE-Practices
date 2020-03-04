from Seq1 import Seq
import socket
import termcolor

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"

seq_list = ["TGTGAACATTCTGCACAGGTCTCTGGCTGCGCCTGGGCGGGTTTCTT", "CAGGAGGGGACTGTCTGTGTTCTCCCTCCCTCCGAGCTCCAGCCTTC",
            "CTCCCAGCTCCCTGGAGTCTCTCACGTAGAATGTCCTCTCCACCCC", "GAACTCCTGCAGGTTCTGCAGGCCACGGCTGGCCCCCCTCGAAAGT",
            "CTGCAGGGGGACGCTTGAAAGTTGCTGGAGGAGCCGGGGGGAA"]

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()

    else:

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()
        argument_command = msg[msg.find(" ") + 1:]
        response = "ERROR"

        # PING command
        if "PING" in msg:
            response = "OK!\n"

        # GET command
        elif "GET" in msg:
            response = seq_list[int(argument_command)]

        # INFO command
        elif "INFO" in msg:
            seq_info = Seq(argument_command)
            count_bases_string = ""
            for base, count in seq_info.count().items():
                s_base = str(base) + ": " + str(count) + " (" + str(
                    round(count / seq_info.len() * 100, 2)) + "%)" + "\n"
                count_bases_string += s_base

            response = ("Sequence: " + str(seq_info) + "\n" +
                        "Total length: " + str(seq_info.len()) + "\n" +
                        count_bases_string)

        elif "COMP" in msg:
            seq_comp = Seq(argument_command)
            response = seq_comp.complement() + "\n"

        elif "REV" in msg:
            seq_rev = Seq(argument_command)
            response = seq_rev.reverse() + "\n"

        elif "GENE" in msg:
            gene = argument_command
            s = Seq()
            s.read_fasta("../Session-04/" + gene + ".txt")
            response = str(s) + "\n"

        # -- The message has to be encoded into bytes
        # Server Console

        termcolor.cprint(msg[:msg.find(" ")], "green")
        print(response)

        # Client console
        cs.send(response.encode())
        # -- Close the data socket
        cs.close()
