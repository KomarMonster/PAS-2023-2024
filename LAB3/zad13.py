import socket

hex_data = "ed740b550024effd70726f6772616d6d696e6720696e20707974686f6e2069732066756e"

bytes_data = bytes.fromhex(hex_data)

src_port = int.from_bytes(bytes_data[0:2], byteorder='big')
dst_port = int.from_bytes(bytes_data[2:4], byteorder='big')
length = int.from_bytes(bytes_data[4:6], byteorder='big')
data = bytes_data[8:].decode('utf-8')

result = f"zad13odp;src;{src_port};dst;{dst_port};data;{data}"

server_address = ("127.0.0.1", 2909)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(server_address)
print(result)
try:
    sock.send(result.encode('utf-8'))
    print(sock.recv(1024).decode('utf-8'))
except socket.error as e:
    print(f'Blad : {e}')
finally:
    sock.close()
