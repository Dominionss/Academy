import socket
import threading


def handle_client(client_socket, client_address):
    print(f"Connection established with {client_address}")
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received from {client_address}: {data.decode('utf-8')}")
            client_socket.send(data)

        except Exception as error:
            print(f"Error with {client_address}: {error}")
            break

    print(f"Connection closed with {client_address}")
    client_socket.close()


def start_server(host='127.0.0.1', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        try:
            client_socket, client_address = server_socket.accept()

            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()

        except KeyboardInterrupt:
            print("Server is shutting down...")
            break
        except Exception as error:
            print(f"Error: {error}")
            break


    server_socket.close()
    print("Server closed.")


if __name__ == "__main__":
    start_server()
