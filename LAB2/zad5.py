import socket

address = '127.0.0.1'
port = 2901

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(5)

try:
    sock.connect((address, port))
    while True:
        message = input("Wpisz wiadomosc: ")
        if message == '': break
        sock.send(message.encode())
        response = sock.recv(1024)
        print(response.decode())

except socket.timeout:
    print('Blad: Timeout')

except socket.error as e:
    print(f'Blad : {e}')

finally:
    sock.close()
