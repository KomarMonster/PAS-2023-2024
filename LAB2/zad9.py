import socket

# address = '212.182.24.27'
address = '127.0.0.1'
port = 2906

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(5)

try:
    sock.connect((address, port))
    message = input('Podaj adres IP: ')
    sock.send(message.encode())

    response = sock.recv(1024)
    print(response.decode())

except socket.timeout:
    print('Blad: Timeout')

except socket.error as e:
    print(f'Blad : {e}')

finally:
    sock.close()
