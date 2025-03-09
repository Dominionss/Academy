import socket
from multiprocessing import Process
from multithreading_tasks import handle_client


def start_server(host='127.0.0.1', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        try:
            client_socket, client_address = server_socket.accept()

            client_process = Process(target=handle_client, args=(client_socket, client_address))
            client_process.start()
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