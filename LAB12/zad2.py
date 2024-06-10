import socket
import threading
import logging
from datetime import datetime

HOST = '127.0.0.1'
PORT = 65432

logging.basicConfig(filename='server_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')


def handle_client(client_socket, client_address):
    try:
        while True:
            data = client_socket.recv(1024)
            logging.info(f"Otrzmano wiadomosc: {data.decode()} od {client_address[0]}:{client_address[1]}")
            if not data:
                break
            client_socket.sendall(data)
    finally:
        client_socket.close()
        logging.info(f"Polaczenie zamkniete z: {client_address[0]}:{client_address[1]}")


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

try:
    while True:
        client_socket, client_address = server_socket.accept()
        logging.info(f"Nawiazano polaczenie z: {client_address[0]}:{client_address[1]}")

        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()
except KeyboardInterrupt:
    server_socket.close()
    logging.info("Serwer zamkniety")
finally:
    server_socket.close()
    logging.info("Serwer zamkniety")
