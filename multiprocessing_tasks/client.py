import socket
from multiprocessing import Process


def send_messages(host, port, client_id):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        print(f"Client {client_id} connected to server at {host}:{port}")

        message = f"Message from client {client_id}"

        client_socket.sendall(message.encode('utf-8'))
        print(f"Client {client_id} sent: {message}")

        data = client_socket.recv(1024)
        print(f"Client {client_id} received: {data.decode('utf-8')}")

    except Exception as error:
        print(f"Client {client_id} error: {error}")
    finally:
        client_socket.close()
        print(f"Client {client_id} connection closed.")


def start_clients(host='127.0.0.1', port=65432, num_clients=3):
    processes = []

    for client_id in range(num_clients):
        process = Process(target=send_messages, args=(host, port, client_id))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("All clients have finished.")


if __name__ == "__main__":
    start_clients()