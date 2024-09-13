# server.py
import socket
import threading

# Configuración del servidor
HOST = '127.0.0.1'
PORT = 65432

# Lista de clientes conectados
clients = []

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Mensaje recibido: {message}")
            # Reenvía el mensaje a todos los clientes
            for client in clients:
                if client != client_socket:
                    client.send(message.encode('utf-8'))
        except:
            break
    client_socket.close()
    clients.remove(client_socket)
    print("Cliente desconectado")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Servidor escuchando en {HOST}:{PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Cliente conectado: {addr}")
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    start_server()


