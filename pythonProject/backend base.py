import os
import socket
import threading
import time
import re

credentials = {'anshumaan#':'anshumaan'}

hostname = socket.gethostname()
addresses = socket.getaddrinfo(hostname, None, socket.AF_INET6)
ipv6_address = addresses[1][4][0]
ports = [12346,12347]

class Server(socket.socket):

    def __init__(self, host=ipv6_address, port1=12347, port2=12346):
        super().__init__(socket.AF_INET6, socket.SOCK_STREAM)
        self.host = host
        self.port1 = port1
        self.port2 = port2

    def start(self):
        print('DNS redirector Activated')
        print('Servers started on ports:', self.port1, 'and', self.port2)
        DNSserver = threading.Thread(target=self.DNS)
        server1_thread = threading.Thread(target=self.server1)
        server2_thread = threading.Thread(target=self.server2)

        DNSserver.start()
        server1_thread.start()
        server2_thread.start()

    def server1(self):
        self.server1_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
        self.server1_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server1_socket.bind((self.host, self.port1, 0, 0))
        self.server1_socket.listen(5)

        print(f"Server 1 listening on port: {self.port1}")

        while True:
            self.client1_socket, addr = self.server1_socket.accept()
            print(f"Connection from {addr} has been established.")
            t1 = threading.Thread(target=self.processing1)
            t1.start()

    def server2(self):
        self.server2_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
        self.server2_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server2_socket.bind((self.host, self.port2, 0, 0))
        self.server2_socket.listen(5)

        print(f"Server 2 listening on port: {self.port2}")

        while True:
            self.client2_socket, addr = self.server2_socket.accept()
            print(f"Connection from {addr} has been established.")
            t4 = threading.Thread(target=self.processing2)
            t4.start()

    def processing1(self):
        t3 = threading.Thread(target=self.prompt1)
        t6 = threading.Thread(target=self.cache1promt)
        t3.start()
        t6.start()
        t3.join()
        t6.join()
    def processing2(self):
        t5 = threading.Thread(target=self.prompt2)
        t7 = threading.Thread(target=self.cache2promt)
        t5.start()
        t7.start()
        t5.join()
        t7.join()
    def prompt1(self):
        n = 1
        self.cache1={}
        self.cache1sent={}
        while True:
            try:
                received_data = self.client1_socket.recv(2048).decode()
                if not received_data:
                    break
                print(f'Received client1: {received_data}')
                try:
                    self.client2_socket.send(received_data.encode())
                    self.cache1sent[(time.time())]=received_data
                except (AttributeError):
                    print("Second Client Hasn't Established the Connection With the Server Yet")
                    self.cache1[(time.time())]=received_data
                    continue
            except (ConnectionError, ConnectionAbortedError):
                print("Connection closed by client1.")
                break

    def prompt2(self):
        self.cache2={}
        self.cache2sent={}
        while True:
            try:
                received_data = self.client2_socket.recv(2048).decode()
                if not received_data:
                    break
                print(f'Received client2: {received_data}')
                try:
                    self.client1_socket.send(received_data.encode())
                    self.cache2sent[(time.time())]=received_data
                except (AttributeError):
                    print("Second Client Hasn't Established the Connection With the Server Yet")
                    self.cache2[(time.time())]=received_data
                    continue
            except (ConnectionError, ConnectionAbortedError):
                print("Connection closed by client2.")
                break

    def cache1promt(self):
        while True:
            try:
                for i in self.cache1.keys():
                    time.sleep(0.2)
                    if i in self.cache1sent.keys():
                        continue
                    else:
                        try:
                            self.client2_socket.send(self.cache1[i].encode())
                            self.cache1sent[i]=self.cache1[i]
                        except (AttributeError):
                            continue
            except (ConnectionError, ConnectionAbortedError, RuntimeError):
                continue

    def cache2promt(self):
        while True:
            try:
                for i in self.cache2.keys():
                    time.sleep(0.2)
                    if i in self.cache2sent.keys():
                        continue
                    else:
                        try:
                            self.client1_socket.send(self.cache2[i].encode())
                            self.cache2sent[i]=self.cache2[i]
                        except (AttributeError):
                            continue
            except (ConnectionError, ConnectionAbortedError, RuntimeError):
                continue

    def DNS(self):
        self.DNS_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
        self.DNS_socket.bind((self.host,12345, 0, 0))
        self.DNS_socket.listen(5)
        print("DNS activated")
        n=0
        while True:
            self.DNSclient_scoket, addr = self.DNS_socket.accept()
            print(f"Connection from {addr} has been requested, waiting for login or Registration")
            logorreg = self.DNSclient_scoket.recv(2048).decode()

            if(logorreg=='login'):
                print(f"Login requested by {addr}")
                cred = self.DNSclient_scoket.recv(2048).decode()
                user = re.search("(^.*?#)", cred)
                passw = re.search("[^#]*$", cred)
                try:
                    if (credentials[user.group(0)] == passw.group(0)):
                        yes = '1'
                        self.DNSclient_scoket.sendall(yes.encode())
                        req = self.DNSclient_scoket.recv(2048).decode()
                        if req:
                            if (req == 'sendport'):
                                self.DNSclient_scoket.send(str(ports[n]).encode())
                                n = n + 1
                            else:
                                continue
                        else:
                            continue
                    elif (credentials[user.group(0)] != passw.group(0)):
                        print(f"Crendentials Not Match failure for client {addr}")
                        self.DNSclient_scoket.send(("Credfail").encode())
                except (KeyError):
                    print("Account Not found")
                    self.DNSclient_scoket.send(("NAF").encode())

            elif(logorreg=='reg'):
                print(f"Registration Requested by {addr}")
                cred = self.DNSclient_scoket.recv(2048).decode()
                user = re.search("(^.*?#)", cred)
                passw = re.search("[^#]*$", cred)
                if user.group(0) in credentials.keys():
                    print("Registration Failed, Username Exist Already")
                    self.DNSclient_scoket.send(('AAE').encode())
                else:
                    print(f"Registration succeful for {addr}")
                    credentials[user.group(0)]=passw.group(0)
                    print(credentials)
                    self.DNSclient_scoket.send(('success').encode())



if __name__ == '__main__':
    server = Server()
    server.start()
