import socket
import datetime

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"{addr} polaczono")
            while True:
                data = conn.recv(1024)
                # print(data.decode('utf-8'))
                if not data:
                    break
                conn.send(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").encode())
