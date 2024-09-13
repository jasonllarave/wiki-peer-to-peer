# client.py
import socket
import threading
import sys

# Configuración del cliente
HOST = '127.0.0.1'
PORT = 65432

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"\nMensaje recibido: {message}")
                sys.stdout.write("Mensaje> ")
                sys.stdout.flush()
        except:
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print("Conectado al servidor")

    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    while True:
        message = input("Mensaje> ")
        if message:
            client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    start_client()
