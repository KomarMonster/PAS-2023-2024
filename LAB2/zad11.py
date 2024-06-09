import socket

# address = '212.182.24.27'
address = '127.0.0.1'
port = 2908

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((address, port))
    while True:
        message = input('Podaj wiadomosc: ')
        sock.send(message.ljust(20).encode())

        response = sock.recv(1024)
        print(response.decode())

except socket.timeout:
    print('Blad: Timeout')

except socket.error as e:
    print(f'Blad : {e}')

finally:
    sock.close()
