import socket

host = '127.0.0.1'
port = 65432

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((host, port))
    while True:
        message = input("Podaj liczbe od 0 do 10: ")
        sock.send(message.encode())
        data = sock.recv(1024)
        print(data.decode())
except socket.error as e:
    print("Blad: ", e)
finally:
    sock.close()
