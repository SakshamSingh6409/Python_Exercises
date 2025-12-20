# client.py
import socket

HOST = "127.0.0.1"  # server address
PORT = 65432        # same port as server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))          # connect to server
    s.sendall(b"Hello server")       # send bytes
    data = s.recv(1024)              # receive reply

print("Received:", data.decode())
