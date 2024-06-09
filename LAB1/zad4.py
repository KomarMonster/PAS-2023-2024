import re
import sys
import socket

pattern = re.compile("^((25[0-5]|(2[0-4]|1\\d|[1-9]|)\\d)\\.?\\b){4}$")

if len(sys.argv) == 1:
    print("Nie podano adresu IP")
    exit(1)
elif re.match(pattern, sys.argv[1]):
    try:
        address = sys.argv[1]
        hostname = socket.gethostbyaddr(address)[0]
        print(f'Nazwa hosta dla adresu {address} to {hostname}')
    except socket.herror:
        print("Nie znaleziono nazwy hosta")
else:
    print("Adres IP niepoprawny")

