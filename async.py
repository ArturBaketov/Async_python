#асинхронный код без использования библиотек:
#1. Callback. 2. Generator, goroutine. 3. Async await

import socket
from select import select  #для мониторинга изменений состояний файловых объектов и сокетов
# .fileno()
# файловый дескриптор - номер файла, число, которое ассоциируется с конкретным файлом

to_monitor = []
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()

def accept_connection(server_socket):
    #while True:
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)
        #send_message(client_socket)
    to_monitor.append(client_socket) # 2 sockets

def send_message(client_socket):
    #while True:
    request = client_socket.recv(4096)

    if request:
        response = 'hello world\n'.encode()
        client_socket.send(response)
    else:
        client_socket.close()


def event_loop():
    while True:
        ready_to_read, _ ,_ = select(to_monitor, [], []) #read, write, errors
        for sock in ready_to_read:
            if sock is server_socket:
                accept_connection(sock)
            else:
                send_message()

if __name__ == '__main__':
    to_monitor.append(server_socket)
    accept_connection(server_socket)
    event_loop()
