import socket
import threading

HOST = '127.0.0.1'
PORT = 65432


def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        client_socket.sendall(data)
    client_socket.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
try:
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connected to {client_address[0]}:{client_address[1]}")

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()
finally:
    server_socket.close()
