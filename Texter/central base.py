import os
import socket
import threading
import time
import re
import datetime
import ast
import json

current_time = datetime.datetime.now()

credentials = {'anshumaan#':'anshumaan','wani#':'wani'}

hostname = socket.gethostname()
addresses = socket.getaddrinfo(hostname, None, socket.AF_INET6)
ipv6_address = addresses[0][4][0]
print(ipv6_address)
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
        self.server1names = []
        self.server1_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
        self.server1_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server1_socket.bind((self.host, self.port1, 0, 0))
        self.server1_socket.listen(5)

        print(f"Server listening on port: {self.port1}")

        while True:
            self.client1_socket, addr = self.server1_socket.accept()
            print(f"Connection from {addr} has been established.")
            user2 = self.client1_socket.recv(2048).decode()̊
            user1 = self.client1_socket.recv(2048).decode()
            self.server1names.append(user1)
            self.server1names.append(user2)
            t1 = threading.Thread(target=self.processing1)
            t1.start()

    def server2(self):
        self.server2names = []
        self.server2_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
        self.server2_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server2_socket.bind((self.host, self.port2, 0, 0))
        self.server2_socket.listen(5)

        print(f"Server 2 listening on port: {self.port2}")

        while True:
            self.client2_socket, addr = self.server2_socket.accept()
            print(f"Connection from {addr} has been established.")
            user2 = self.client2_socket.recv(2048).decode()
            user1 = self.client2_socket.recv(2048).decode()
            self.server2names.append(user1)
            self.server2names.append(user2)
            t4 = threading.Thread(target=self.processing2)
            t4.start()

    def processing1(self):
        user = self.server1names[0]
        user2 = self.server1names[1]
        t3 = threading.Thread(target=self.prompt1)
        t6 = threading.Thread(target=self.tcache1promt, args=(user,user2))
        t3.start()
        t6.start()
        t3.join()
        t6.join()

    def processing2(self):
        user = self.server2names[0]
        user2 = self.server2names[1]
        t5 = threading.Thread(target=self.prompt2)
        t7 = threading.Thread(target=self.tcache2promt, args=(user,user2))
        t5.start()
        t7.start()
        t5.join()
        t7.join()

    def prompt1(self):
        user = self.server1names[0]
        user2 = self.server1names[1]
        while True:
            try:
                received_data = self.client1_socket.recv(2048).decode()
                if not received_data:
                    break
                print(f'Received client1: {received_data}')
                try:
                    self.client2_socket.send(received_data.encode())
                    tcache[user2][current_time] = [received_data, 1, user]
                except (AttributeError):
                    print("Second Client Hasn't Established the Connection With the Server Yet")
                    tcache[user2][current_time] = [received_data, 0, user]
                    continue
            except (ConnectionError, ConnectionAbortedError):
                print("Connection closed by client1.")
                break

    def prompt2(self):
        user = self.server2names[0]
        user2 = self.server2names[1]
        while True:
            try:
                received_data = self.client2_socket.recv(2048).decode()
                if not received_data:
                    break
                print(f'Received client2: {received_data}')
                try:
                    self.client1_socket.send(received_data.encode())
                    tcache[user2][current_time] = [received_data, 1, user]
                except (AttributeError):
                    print("Second Client Hasn't Established the Connection With the Server Yet")
                    tcache[user2][current_time] = [received_data, 0, user]
                    continue
            except (ConnectionError, ConnectionAbortedError):
                print("Connection closed by client2.")
                break

    def tcache1promt(self,user,user2):
        while True:
            try:
                for i in tcache[user].keys():
                    if tcache[user][i][2]==user2:
                        if tcache[user][i][1] == 0:
                            time.sleep(0.1)
                            try:
                                self.client2_socket.send(tcache[user][i][0].encode())
                            except (AttributeError):
                                continue
                            tcache[user][i][1] = 1
                        else:
                            continue
                    else:
                        continue
            except (ConnectionRefusedError, ConnectionError, RuntimeError):
                continue

    def tcache2promt(self,user,user2):
        while True:
            try:
                for i in tcache[user].keys():
                    if tcache[user][i][2]==user2:
                        if tcache[user][i][1] == 0:
                            time.sleep(0.1)
                            try:
                                self.client2_socket.send(tcache[user][i][0].encode())
                            except (AttributeError):
                                continue
                            tcache[user][i][1] = 1
                        else:
                            continue
                    else:
                        continue
            except (ConnectionRefusedError, ConnectionError, RuntimeError):
                continue

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
        self.users=[]
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
                                self.users.append(user.group(0))
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
    with open('/Users/anshumaansoni/PycharmProjects/pythonProject/text cache txt', 'r') as file:
        text = file.read()
        tcache = ast.literal_eval(text)
    server = Server()
    server.start()
    with open('/Users/anshumaansoni/PycharmProjects/pythonProject/text cache txt', 'w') as file:
        file.write(json.dumps(tcache))