import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    while True:
        data1, addr = s.recvfrom(1024)
        print(f"Otrzymano dane: {data1} od {addr}")
        data2, addr = s.recvfrom(1024)
        print(f"Otrzymano dane: {data2} od {addr}")
        data3, addr = s.recvfrom(1024)
        print(f"Otrzymano dane: {data3} od {addr}")
        if data1.decode().isnumeric() and data3.decode().isnumeric() and data2.decode() in ['+', '-', '*', '/']:
            data = str(eval(data1.decode() + data2.decode() + data3.decode())).encode()
        s.sendto(data, addr)