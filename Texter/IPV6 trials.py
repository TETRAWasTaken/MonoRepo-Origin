import socket

host = "2409:40c4:e5:15ac:8000::"
port = 12345

clientsocket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
clientsocket.connect((host,port,0,0))

while True:
    a = clientsocket.recv(2048).decode()
    print(a)
    b = input()
    clientsocket.sendall((b.encode()))