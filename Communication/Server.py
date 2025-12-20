# server.py
import socket

HOST = "127.0.0.1"   # listen on local machine
PORT = 65432         # any free port > 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))      # attach to address
    s.listen()                # start listening
    print("Waiting for connection...")
    conn, addr = s.accept()   # block until client connects
    with conn:
        print("Connected by", addr)
        data = conn.recv(1024)        # receive bytes
        print("Got:", data.decode())
        conn.sendall(b"Hello client") # send reply
