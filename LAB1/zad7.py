import socket

HOST = '127.0.0.1'
PORTS = range(80, 65535)

for PORT in PORTS:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((HOST, PORT))
    if result == 0:
        print(f'Port {PORT} jest otwarty')
    else:
        print(f'Port {PORT} jest zamkniety')
    s.close()
