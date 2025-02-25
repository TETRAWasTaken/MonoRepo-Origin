import wx

class LoginRegistrationFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(300, 150))

        self.panel = wx.Panel(self)

        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.login_button = wx.Button(self.panel, label="Login")
        self.login_button.Bind(wx.EVT_BUTTON, self.on_login_click)  # Bind click event
        self.sizer.Add(self.login_button, 0, wx.ALL | wx.CENTER, 5)  # Add button with padding

        self.register_button = wx.Button(self.panel, label="Register")
        self.register_button.Bind(wx.EVT_BUTTON, self.on_register_click)  # Bind click event
        self.sizer.Add(self.register_button, 0, wx.ALL | wx.CENTER, 5)  # Add button with padding

        self.panel.SetSizer(self.sizer)

    def on_login_click(self, event):
        print("Login button clicked!")
        self.login_button.Destroy()
        self.register_button.Destroy()
        self.user_text = wx.StaticText(self.panel, label="Username - ", pos=(50, 25))
        self.sizer.Add(self.user_text, 0, wx.ALIGN_CENTER, 5)
        self.message = wx.TextCtrl(self.panel, pos=(115, 25))
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        hsizer.Add(self.message, 1, wx.EXPAND, 5)

        self.pass_text = wx.StaticText(self.panel, label="Password - ", pos=(50, 55))
        self.sizer.Add(self.pass_text, 0, wx.ALIGN_CENTER, 5)
        self.message2 = wx.TextCtrl(self.panel, pos=(115, 55))
        hsizer.Add(self.message2, 1, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(hsizer, 1, wx.EXPAND | wx.ALL, 5)

        username = self.message.GetValue()
        passw = self.message2.GetValue()
        req = username + '#' + passw
        self.clientDNS_socket.sendall(req.encode())
        reqr = self.clientDNS_socket.recv(2048).decode()

        if reqr:
            if (reqr == '1'):
                reqr1 = 'sendport'
                self.clientDNS_socket.send(reqr1.encode())
                portno = self.clientDNS_socket.recv(2048).decode()
                self.port = int(portno)
                self.login_panel.Destroy()
                frame = TextMessagingGUI()
                frame.client()
                app.MainLoop()

            elif (reqr == 'Credfail'):
                print("Username, Password dont match ( Credfail Error) ")
            else:
                print("No Account Found !!")
        else:
            print("Server did not respond")

    def on_register_click(self, event):
      # Handle registration button click (placeholder for your registration logic)
      print("Register button clicked!")





if __name__ == "__main__":
    app = wx.App()
    frame = LoginRegistrationFrame(None, "Login or Register")
    frame.Show()
    app.MainLoop()
