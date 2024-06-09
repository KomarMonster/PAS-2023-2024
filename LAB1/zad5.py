import sys
import socket

if len(sys.argv) == 1:
    print("Nie podano adresu IP")
    exit(1)
else:
    try:
        hostname = sys.argv[1]
        address = socket.gethostbyname(hostname)
        print(f'Adres hosta dla nazwy {hostname} to {address}')
    except socket.herror:
        print("Nie znaleziono nazwy hosta")
