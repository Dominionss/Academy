import socket
from caesar import caesar_cipher


def start_server(host='127.0.0.1', port=65432):
    """Starts the echo server that encrypts messages using the Caesar Cipher."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")

        while True:
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Connected to {client_address}")

                data = client_socket.recv(1024).decode('utf-8')
                key, message = data.split('|', 1)
                key = int(key)

                encrypted_message = caesar_cipher(message, key)
                print(f"Received: {message} | Encrypted: {encrypted_message}")

                client_socket.sendall(encrypted_message.encode('utf-8'))


if __name__ == "__main__":
    start_server()
