import threading
import socket

print("Enter the Server Ip : ")
IP = input('')
print("Enter the port no. : ")
port = int(input(''))

def send(client_socket):
    while True:
        try:
            message = input("You: ")
            if message:
                client_socket.sendall(message.encode())
            else:
                break

        except (ConnectionError, ConnectionAbortedError):
            print("Connection closed by client.")
            break

def receive(client_socket):
    while True:
        try:
            received_data = client_socket.recv(2048).decode()
            if not received_data:
                continue
            else:
                print(f'Server: {received_data}')

        except (ConnectionError, ConnectionAbortedError):
            print("Connection closed by client.")
            break

def client():
    try:
        client_socket = socket.socket()
        client_socket.connect((IP, port))
        print("Connected!")

        receive_thread = threading.Thread(target=receive, args=(client_socket,))
        send_thread = threading.Thread(target=send, args=(client_socket,))

        receive_thread.start()
        send_thread.start()

        receive_thread.join()
        send_thread.join()

    except ConnectionRefusedError:
        print("Target Refused to Connect")

    except (ConnectionError, ConnectionAbortedError):
        print("Connection closed by client.")

if __name__ == "__main__":
    client()
