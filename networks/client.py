import socket

def start_client(host='127.0.0.1', port=65432):
    """ Starts the client to interact with the echo server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        key = input("Enter the encryption key (integer): ")
        message = input("Enter the message to encrypt: ")

        data = f"{key}|{message}"
        client_socket.sendall(data.encode('utf-8'))

        encrypted_message = client_socket.recv(1024).decode('utf-8')
        print(f"Encrypted message from server: {encrypted_message}")

if __name__ == "__main__":
    start_client()
