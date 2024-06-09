import socket

hex_data = "4500004ef7fa400038069d33d4b6181bc0a800020b54b9a6fbf93c57c10a06c1801800e3ce9c00000101080a03a6eb01000bf8e56e6574776f726b2070726f6772616d6d696e672069732066756e"

bytes_data = bytes.fromhex(hex_data)

ip_ver = bytes_data[0] >> 4
src_ip = '.'.join(map(str, bytes_data[12:16]))
dst_ip = '.'.join(map(str, bytes_data[16:20]))
protocol = bytes_data[9]
src_port = int.from_bytes(bytes_data[20:22], byteorder='big')
dst_port = int.from_bytes(bytes_data[22:24], byteorder='big')


tcp_offset = 20
tcp_src_port = int.from_bytes(bytes_data[tcp_offset + 0:tcp_offset + 2], byteorder='big')
tcp_dst_port = int.from_bytes(bytes_data[tcp_offset + 2:tcp_offset + 4], byteorder='big')
tcp_data_offset = (bytes_data[tcp_offset + 12] >> 4) * 4

data = bytes_data[tcp_offset + tcp_data_offset:].decode('utf-8')

server_address = ('127.0.0.1', 2911)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(server_address)

message_a = f"zad15odpA;ver;{ip_ver};srcip;{src_ip};dstip;{dst_ip};type;{protocol}"
print(message_a)
sock.send(message_a.encode())
response_a = sock.recv(1024).decode()
print(f"Odpowiedz A: {response_a}")

if response_a == "TAK":
    message_b = f"zad15odpB;srcport;{src_port};dstport;{dst_port};data;{data}"
    print(message_b)
    sock.send(message_b.encode())
    response_b = sock.recv(1024).decode()
    print(f"Odpowiedz B: {response_b}")