import asyncio


async def handle_client(reader, writer):
    client_address = writer.get_extra_info('peername')
    print(f"Connection established with {client_address}")

    try:
        while True:
            data = await reader.read(1024)
            if not data:
                break

            message = data.decode('utf-8')
            print(f"Received from {client_address}: {message}")
            writer.write(data)
            await writer.drain()

    except Exception as error:
        print(f"Error with {client_address}: {error}")
    finally:
        print(f"Connection closed with {client_address}")
        writer.close()
        await writer.wait_closed()

async def start_server(host='127.0.0.1', port=65432):
    try:
        server = await asyncio.start_server(handle_client, host, port)
        print(f"Server listening on {host}:{port}")

        async with server:
            await server.serve_forever()
    except Exception as error:
        print(f"Server error: {error}")
    finally:
        print("Server closed.")


if __name__ == "__main__":
    asyncio.run(start_server())