import socket

def start_client(host='127.0.0.1', port=65432):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        while True:
            message = input("Enter a message (or 'exit' to quit): ")
            if message.lower() == 'exit':
                break

            client_socket.sendall(message.encode('utf-8'))

            data = client_socket.recv(1024)
            print(f"Received from server: {data.decode('utf-8')}")

    except Exception as error:
        print(f"Error: {error}")
    finally:
        client_socket.close()
        print("Connection closed.")


if __name__ == "__main__":
    start_client()