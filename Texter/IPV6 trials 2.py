import socket

Host = "2401:4900:8823:397d:31a8:5922:99ac:5deb"
port =12345

serversocket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
serversocket.bind((Host,port,0,0))
serversocket.listen(5)
while True:
   client1_socket, addr = serversocket.accept()
   print(f"Connection from {addr} has been established.")
   a = input()
   client1_socket.sendall((a.encode()))
   b = client1_socket.recv(2048).decode()
   print(b)
