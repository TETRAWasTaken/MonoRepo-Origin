import socket
import time
import threading
def send(client_socket):
    while True:
        sen=input('')
        try:
            client_socket.sendall(sen.encode())
        except (ConnectionError, ConnectionAbortedError):
            print("Connection closed by client.")
            break
def prompt(client_socket):
    while True:
        try:
            received_data = client_socket.recv(2048).decode()
            if not received_data:
                break
            print(f'Received String: {received_data}')
        except (ConnectionError, ConnectionAbortedError):
            print("Connection closed by client.")
            break

def processing(client_socket):
    t3 = threading.Thread(target=prompt, args=(client_socket,))
    t2 = threading.Thread(target=send, args=(client_socket,))

    t3.start()
    t2.start()

    t3.join()
    t2.join()

def client():
    client_socket = socket.socket()
    client_socket.connect(('192.168.1.8', 12346))

    t1 = threading.Thread(target=processing, args=(client_socket,))
    t1.start()

if __name__ == "__main__":
    client()