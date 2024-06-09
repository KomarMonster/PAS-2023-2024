import socket

HOST = '127.0.0.1'
PORT = 65432
server_address = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)
try:
    sock.connect(server_address)
    print("Polaczono z serwerem")
    try:
        service = socket.getservbyport(PORT)
    except OSError:
        service = "Nieznana usluga"
    print(f"Na porcie {PORT} dziala: {service}")
except socket.error as e:
    print(f'Blad: {e}')


sock.close()
