import random
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            number = random.randint(1, 10)
            print(f"{addr} polaczono")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                if data.decode() == str(number):
                    conn.send("Gratulacje, zgadles liczbe!".encode())
                    number = random.randint(1, 10)
                elif data.decode() > str(number):
                    conn.send("Za duzo!".encode())
                else:
                    conn.send("Za malo!".encode())
