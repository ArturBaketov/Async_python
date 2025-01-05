#асинхронный код без использования библиотек:
#1. Callback. 2. Generator, goroutine. 3. Async await
import socket
import  selectors #для мониторинга изменений состояний файловых объектов и сокетов
# .fileno()
# файловый дескриптор - номер файла, число, которое ассоциируется с конкретным файлом

selector = selectors.DefaultSelector()

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()
    # регистрация сокета для дальнейшей выборки, когда сможет читать или записывать .file_no, args, data
    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)

def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)

    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)

def send_message(client_socket):
    request = client_socket.recv(4096)

    if request:
        response = 'hello world\n'.encode()
        client_socket.send(response)
    else:
        selector.unregister(client_socket) #Снимаем с регистрации
        client_socket.close()

def event_loop():
    while True:
        events = selector.select() #(key, events)
        #selectorKey fileobj, events, data
        for key, _ in events:
            callback = key.data
            callback(key.fileobj)

if __name__ == '__main__':
    server()
    event_loop()

