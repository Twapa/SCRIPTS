import socket
import json


c_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c_sock.connect(("127.0.0.1", 5000))
c_sock.send("Test message".encode("ascii"))
data = c_sock.recv(1024)
response = json.loads(data)
print (json.dumps(response, indent=3))