import socket

hex_data = "0b54898b1f9a18ecbbb164f2801800e3677100000101080a02c1a4ee001a4cee68656c6c6f203a29"

bytes_data = bytes.fromhex(hex_data)

src_port = int.from_bytes(bytes_data[0:2], byteorder='big')
dst_port = int.from_bytes(bytes_data[2:4], byteorder='big')
data_offset = (bytes_data[12] >> 4) * 4

data = bytes_data[data_offset:].decode('utf-8')

result = f"zad14odp;src;{src_port};dst;{dst_port};data;{data}"

print(result)
server_address = ('127.0.0.1', 2910)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(server_address)
try:
    sock.send(result.encode('utf-8'))
    print(sock.recv(1024).decode('utf-8'))
except socket.error as e:
    print(f'Blad : {e}')
finally:
    sock.close()

