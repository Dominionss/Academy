import asyncio


async def echo_client(host='127.0.0.1', port=65432):
    try:
        reader, writer = await asyncio.open_connection(host, port)
        print(f"Connected to server at {host}:{port}")

        while True:
            message = input("Enter a message (or 'exit' to quit): ")
            if message.lower() == 'exit':
                break

            writer.write(message.encode('utf-8'))
            await writer.drain()  # Ensure the data is sent

            data = await reader.read(1024)
            if not data:
                print("Server closed the connection.")
                break
            print(f"Received from server: {data.decode('utf-8')}")

    except ConnectionRefusedError:
        print(f"Could not connect to server at {host}:{port}")
    except Exception as error:
        print(f"Error: {error}")
    finally:
        print("Closing the connection...")
        writer.close()
        await writer.wait_closed()
        print("Connection closed.")


if __name__ == "__main__":
    asyncio.run(echo_client())
