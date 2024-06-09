import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    while True:
        data, addr = s.recvfrom(1024)
        print(f"Otrzymano dane: {data} od {addr}")
        data = socket.gethostbyaddr(data.decode())[0]
        s.sendto(data.encode(), addr)