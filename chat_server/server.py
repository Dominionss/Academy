import asyncio


ADMIN_NAME = 'user123'
clients = {}


async def broadcast(message, sender=None):
    for name, writer in clients.items():
        if name != sender:
            writer.write(f'{message}\n'.encode())
            await writer.drain()


async def private_message(sender, recipient, message):
    if recipient in clients:
        clients[recipient].write(f'[PM from {sender}]: {message}\n'.encode())
        await clients[recipient].drain()
    else:
        clients[sender].write(f'User {recipient} not found.\n'.encode())
        await clients[sender].drain()


async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')

    await writer.drain()
    name = (await reader.read(100)).decode().strip()

    if name in clients:
        writer.write(b'Name already taken. Disconnecting.\n')
        await writer.drain()
        writer.close()
        await writer.wait_closed()
        return

    clients[name] = writer
    print(f'{name} connected from {addr}')
    await broadcast(f'{name} joined the chat.')

    try:
        while True:
            data = await reader.read(1024)
            if not data:
                break

            message = data.decode().strip()

            if message == 'QUIT':
                await broadcast(f'{name} left the chat.')
                break

            elif message.startswith('pm:'):
                try:
                    _, recipient, msg = message.split(':', 2)
                    await private_message(name, recipient, msg)
                except ValueError:
                    writer.write(b'Invalid private message format. Use pm:recipient:message\n')
                    await writer.drain()

            elif name == ADMIN_NAME and message.startswith('kick:'):
                _, target_name = message.split(':', 1)
                if target_name in clients and target_name != ADMIN_NAME:
                    try:
                        clients[target_name].write(b'You have been kicked by the admin.\n')
                        await clients[target_name].drain()
                    except Exception as e:
                        print(f"Error sending kick message: {e}")

                    try:
                        clients[target_name].close()
                        await clients[target_name].wait_closed()
                    except Exception as e:
                        print(f"Error closing connection: {e}")
                    if target_name in clients:
                        del clients[target_name]
                        await broadcast(f'{target_name} has been kicked by the admin.')
                else:
                    writer.write(b'Cannot kick this user.\n')
                    await writer.drain()
            else:
                await broadcast(f'{name}: {message}', sender=name)

    except Exception as e:
        print(f'Error: {e}')
    finally:
        if name in clients:
            del clients[name]
            writer.close()
            await writer.wait_closed()
            print(f'{name} disconnected.')


async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    print('Server started on 127.0.0.1:8888')

    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())
