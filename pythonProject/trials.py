import wx
import socket
import threading
def enct(string):
    key = {'a': '@', 'b': '^', 'c': '&', 'd': '*', 'e': '/', 'f': '.', 'g': '{', 'h': '}', 'i': '+', 'j': '=', 'k': '#',
           'l': '!', 'm': '<', 'n': '_', 'o': '|', 'p': '~', 'q': '$', 'r': '%', 's': '`', 't': '(', 'u': ')', 'v': '-',
           'w': '2', 'x': '3', 'y': '6', 'z': '8', ' ': '0'}
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

class LoginRegistrationFrame(wx.Frame):

    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(400, 500))

        self.panel = wx.Panel(self)

        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.login_button = wx.Button(self.panel, label="Login")
        self.login_button.Bind(wx.EVT_BUTTON, self.on_login_click)
        self.sizer.Add(self.login_button, 0, wx.ALL | wx.CENTER, 5)

        self.register_button = wx.Button(self.panel, label="Register")
        self.register_button.Bind(wx.EVT_BUTTON, self.on_register_click)
        self.sizer.Add(self.register_button, 0, wx.ALL | wx.CENTER, 5)

        self.message = wx.TextCtrl(self.panel, pos=(100, 10))
        self.message2 = wx.TextCtrl(self.panel, pos=(100, 40))
        self.user_text = wx.StaticText(self.panel, label="Username - ", pos=(25, 10))
        self.sizer.Add(self.user_text, 0, wx.ALL, 5)
        self.sizer.Add(self.message, 0, wx.ALL, 5)

        self.pass_text = wx.StaticText(self.panel, label="Password - ", pos=(25, 40))
        self.sizer.Add(self.pass_text, 0, wx.ALL, 5)
        self.sizer.Add(self.message2, 0, wx.ALL, 5)

        self.login2_button = wx.Button(self.panel, label='Login', pos=(100,60))
        self.login2_button.Bind(wx.EVT_BUTTON, self.logth)
        self.sizer.Add(self.login2_button, 0, wx.ALL, 5)

        self.panel.SetSizer(self.sizer)
        self.Show(True)

        self.message.Hide()
        self.message2.Hide()
        self.user_text.Hide()
        self.pass_text.Hide()
        self.login2_button.Hide()

    def logth(self, event):
        logthh = threading.Thread(target=self.login)
        logthh.start()

    def login(self):
            username = self.message.GetValue()
            passw = self.message2.GetValue()
            if username:
                req = username + '#' + passw
                self.clientDNS_socket.sendall(req.encode())
                reqr = self.clientDNS_socket.recv(2048).decode()

                if reqr:
                    if (reqr == '1'):
                        reqr1 = 'sendport'
                        self.clientDNS_socket.send(reqr1.encode())
                        portno = self.clientDNS_socket.recv(2048).decode()
                        self.port = int(portno)
                        print(portno)
                        self.Close()
                        App = wx.App(False)
                        frame1 = TextMessagingGUI()
                        frame1.client(self.port)
                        App.MainLoop()

                    elif (reqr == 'Credfail'):
                        print("Username, Password dont match ( Credfail Error) ")
                    else:
                        print("No Account Found !!")
                else:
                    print("Server did not respond")

    def on_login_click(self, event):
        print("Login button clicked!")
        self.message.Show()
        self.message2.Show()
        self.user_text.Show()
        self.pass_text.Show()
        self.login2_button.Show()
        self.login_button.Destroy()
        self.register_button.Destroy()
        self.clientDNS_socket.send(('login').encode())
    def on_register_click(self, event):
        print("Register button clicked!")

    def client(self):
        try:
            self.clientDNS_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
            self.clientDNS_socket.connect(('fe80::8e2f:154e:ad00:b28d%21', 12345, 0, 0))

        except ConnectionRefusedError:
            print("Tagret Refused to Connect")

        except (ConnectionError, ConnectionAbortedError):
            print("Connection closed by client.")


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

    def send(self, event):
        while True:
            try:
                if self.message_entry.GetValue():
                    txt = wx.CallAfter(self.message_entry.GetValue())
                    txt = enct(txt)
                    self.client_socket.sendall((txt).encode())
                    wx.CallAfter(self.chat_history.AppendText(f"\nMe: {self.message_entry.GetValue()}"))
                    wx.CallAfter(self.message_entry.Clear())
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

    def processing(self):
        t3 = threading.Thread(target=self.prompt) 
        t2 = threading.Thread(target=self.send)

        t3.start()
        t2.start()

        t3.join()
        t2.join()

    def client(self, port):
        try:
            self.client_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
            self.client_socket.connect(('fe80::8e2f:154e:ad00:b28d%21',port,0,0))
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
    frame = LoginRegistrationFrame(None, "Login or Register")
    clienth = threading.Thread(target=frame.client)
    clienth.start()
    app.MainLoop()
