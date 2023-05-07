import socket
import json
import threading

db = []  # a list to serve as a database

def handle_client(connection, address):
    data = connection.recv(1024)
    print("Received {} from {}".format(data, address))
    db.append({'host': address, "data": data})
    response = json.dumps({"status" : "OK", "message" : "Data was saved."})
    connection.sendall(response.encode("ascii"))
    connection.shutdown(socket.SHUT_RDWR)
    connection.close()
    return


def server():
    print("[+] Starting server")
    # create a TCP socket
    srv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # set some socket options
    srv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv_socket.bind(("127.0.0.1", 5000))  # bind socket to loopback address
    srv_socket.listen() # start listening for connections
    while True:
        conn, addr = srv_socket.accept()  # accept an incoming connection
        # delegate handling a client to a thread
        t = threading.Thread(target=handle_client, args=(conn, addr,), daemon = True)
        t.start() # start the thread


def main():
    server()

main()
