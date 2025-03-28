import sys
import asyncio


# send message to server
async def write_messages(writer):
    # enter the name
    name = input("Enter your name: ")
    # read messages from the user and transmit to server
    writer.write(name.encode() + b'\n')
    await writer.drain()

    while True:
        # read from stdin
        message = await asyncio.to_thread(sys.stdin.readline)
        # encode the string message to bytes
        msg_bytes = message.encode()
        # transmit the message to the server
        writer.write(msg_bytes)
        # wait for the buffer to be empty
        await writer.drain()
        # check if the user wants to quit the program
        if message.strip() == 'QUIT':
            # exit the loop
            break
    # report that the program is terminating
    print('Quitting...')


# read messages from the server
async def read_messages(reader):
    # read messages from the server and print to user
    while True:
        # read a message from the server
        result_bytes = await reader.readline()
        # decode response from bytes to a string
        response = result_bytes.decode()
        # report the response to the user
        print(response.strip())
        # check if there is any data, if not, then disconnect
        if not result_bytes:
            break


# echo client
async def main():
    # define the server details
    server_address, server_port = '127.0.0.1', 8888
    # report progress to the user
    print(f'Connecting to {server_address}:{server_port}...')
    # open a connection to the server
    reader, writer = await asyncio.open_connection(server_address, server_port)
    # report progress to the user
    print('Connected.')
    # read and report messages from the server
    read_task = asyncio.create_task(read_messages(reader))
    # write messages to the server
    await write_messages(writer)
    # cancel the read messages task
    read_task.cancel()
    # report progress to the user
    print('Disconnecting from server...')
    # close the stream writer
    writer.close()
    # wait for the tcp connection to close
    await writer.wait_closed()
    # report progress to the user
    print('Done.')


# run the event loop
asyncio.run(main())
