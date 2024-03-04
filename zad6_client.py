import socket

HOST = '127.0.0.1'
PORT = 65432
server_address = (HOST, PORT)

# TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# UDP
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(server_address)


while(True):
    try:
        # TCP
        text = input().encode('utf-8')
        sock.send(text)
        # UDP
        # sock.sendto(message, server_address)

        # TCP
        answer = sock.recv(1024)
        # UDP
        # answer, server = sock.recvfrom(4096)

        print(answer.decode('utf-8'))

    except socket.error as e:
        print(e)

sock.close()
