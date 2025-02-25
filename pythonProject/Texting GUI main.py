import wx
import threading
import socket

print("Enter the Server Ip : ")
IP = input('')
print("Enter the port no. : ")
port = int(input(''))

def enct(string):
    key = {'a': '@', 'b': '^', 'c': '&', 'd': '*', 'e': '/', 'f': '.', 'g': '{', 'h': '}', 'i': '+', 'j': '=', 'k': '#', 'l': '!', 'm': '<', 'n': '_', 'o': '|', 'p': '~', 'q': '$', 'r': '%', 's': '`', 't': '(', 'u': ')', 'v': '-', 'w': '2', 'x': '3', 'y': '6', 'z': '8', ' ': '0'}
    li = []
    for i in string:
      b = key[i]
      li.append(b)
    string = "".join(li)
    return string

def dect(string):
    key = {'@': 'a', '^': 'b', '&': 'c', '*': 'd', '/': 'e', '.': 'f', '{': 'g', '}': 'h', '+': 'i', '=': 'j', '#': 'k', '!': 'l', '<': 'm', '_': 'n', '|': 'o', '~': 'p', '$': 'q', '%': 'r', '`': 's', '(': 't', ')': 'u', '-': 'v', '2': 'w', '3': 'x', '6': 'y', '8': 'z', '0': ' '}
    li = []
    for i in string:
      b = key[i]
      li.append(b)
    string = "".join(li)
    return string
class TextMessagingGUI(wx.Frame):

    def __init__(self, parent=None):
        super().__init__(parent, title="Text Messaging Client")

        central_panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        central_panel.SetSizer(sizer)

        self.chat_history = wx.TextCtrl(central_panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        sizer.Add(self.chat_history, 1, wx.EXPAND | wx.ALL, 5)

        self.message_entry = wx.TextCtrl(central_panel)
        self.send_button = wx.Button(central_panel, label="Send")
        self.send_button.Bind(wx.EVT_BUTTON, self.send)

        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        hsizer.Add(self.message_entry, 1, wx.EXPAND, 5)
        hsizer.Add(self.send_button, 0, wx.HORIZONTAL, 5)
        sizer.Add(hsizer, 0, wx.EXPAND | wx.ALL, 5)

        self.status_bar = wx.StaticText(central_panel, label="Disconnected")
        sizer.Add(self.status_bar, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)
        self.Show(True)

    def userdata(self):
        try:
            self.clientDNS_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
            self.clientDNS_socket.connect((IP, port, 0, 0))

        except ConnectionRefusedError:
            print("Tagret Refused to Connect")

        except (ConnectionError, ConnectionAbortedError):
            print("Connection closed by Server.")

        print("Login or Register as New user  (1/2)")
        stat = int(input())
        if (stat == 1):
            self.clientDNS_socket.send(('login').encode())
            print("Enter your Username")
            username = input().rstrip()
            print("Enter your Password")
            passw = input().rstrip()
            req = username + '#' + passw
            self.clientDNS_socket.sendall(req.encode())
            reqr = self.clientDNS_socket.recv(2048).decode()
            if reqr:
                if (reqr == '1'):
                    reqr1 = 'sendport'
                    self.clientDNS_socket.send(reqr1.encode())
                    portno = self.clientDNS_socket.recv(2048).decode()
                    print('1')
                    self.port = int(portno)
                    self.client()
                elif (reqr == 'Credfail'):
                    print("Username, Password dont match ( Credfail Error) ")
                else:
                    print("No Account Found !!")
            else:
                print("Server did not respond")

        else:
            self.clientDNS_socket.send(('reg').encode())
            print("Set an Username")
            username = input().rstrip()
            print("Set the password")
            passw = input().rstrip()
            req = username+'#'+passw
            self.clientDNS_socket.send(req.encode())
            reqr = self.clientDNS_socket.recv(2048).decode()
            if(reqr=='AAE'):
                print("Username exists already. try logging in or select a different Username")

            elif(reqr=='success'):
                print("New Account succesfully registered, Please Login Now")

            else:
                print("Error Occured")

    def send(self, event):
        while True:
            try:
                if self.message_entry.GetValue():
                    txt = self.message_entry.GetValue()
                    txt = enct(txt)
                    self.client_socket.sendall((txt).encode())
                    self.chat_history.AppendText(f"\nMe: {self.message_entry.GetValue()}")
                    self.message_entry.Clear()
                else:
                    break

            except (ConnectionError, ConnectionAbortedError):
                print("Connection closed by client.")
                self.status_bar.SetLabelText('Disconnected')
                break

    def prompt(self):
        while True:
            try:
                received_data = self.client_socket.recv(2048).decode()
                received_data = dect(received_data)
                if not received_data:
                    continue
                else:
                    print(f'Received String: {received_data}')
                    self.chat_history.AppendText(f"\nServer : {received_data}")

            except (ConnectionError, ConnectionAbortedError):
                print("Connection closed by client.")
                self.status_bar.SetLabelText('Disconnected')
                break

    def client(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
            self.client_socket.connect((IP,self.port,0,0))
            self.status_bar.SetLabelText('Connected')

            t1 = threading.Thread(target=self.prompt)
            t1.start()

        except ConnectionRefusedError:
            print("Tagret Refused to Connect")
            self.status_bar.SetLabelText("Connection Error")

        except (ConnectionError, ConnectionAbortedError):
            print("Connection closed by client.")
            self.status_bar.SetLabelText('Disconnected')

if __name__ == '__main__':
    app = wx.App(False)
    frame = TextMessagingGUI()
    frame.userdata()
    app.MainLoop()

