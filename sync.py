#асинхронный код без использования библиотек:
#1. Callback. 2. Generator, goroutine. 3. Async await

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()

while True:
    print('Before .accept')
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)

    while True:
        print('Before .recv')
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = 'hello world\n'.encode()
            client_socket.send(response)

    print('Outside inner while loop')
    client_socket.close()