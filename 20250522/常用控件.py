# 引入控件


import wx


# 创建一个窗口类
class MyFrame(wx.Frame):
    #  创建一个事件
    def on_click(self, event):
        dialog = wx.MessageDialog(self, "登陆成功", "提示", wx.OK)
        dialog.ShowModal()

    def clear_text(self, event):
        self.t1.Clear()
        self.t2.Clear()

    def delag(self, event):
        print("delag")

    #  创建一个构造函数
    def __init__(self):
        # 创建一个窗口类
        super().__init__(None, title="wxPython Frame")
        # 创建一个面板
        panel = wx.Panel(self)
        # 创建一个静态文本
        text1 = wx.StaticText(panel, label="请输入账号")
        # 创建一个输入框
        self.t1 = wx.TextCtrl(panel, pos=(150, 50), size=(200, 30))
        # 创建一个静态文本
        text2 = wx.StaticText(panel, label="请输入密码")
        # 创建一个密码输入框，居中对齐
        self.t2 = wx.TextCtrl(panel, size=(200, 30), style=wx.TE_PASSWORD | wx.TE_CENTER)
        # 创建一个按钮
        button = wx.Button(panel, label="登录", size=(100, 30))
        self.Bind(wx.EVT_BUTTON, self.on_click, button)
        button_clear = wx.Button(panel, label="清空", size=(100, 30))
        self.Bind(wx.EVT_BUTTON, self.clear_text, button_clear)
        # 创建一个布局容器
        # 水平布局
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)

        hbox1.Add(text1, 0, wx.EXPAND | wx.ALL, 5)
        hbox1.Add(self.t1, 0, wx.EXPAND | wx.ALIGN_LEFT, 5)

        hbox2.Add(text2, 0, wx.EXPAND | wx.ALL, 5)
        hbox2.Add(self.t2, 0, wx.EXPAND | wx.ALIGN_LEFT, 5)

        hbox3.Add(button, 1, wx.EXPAND | wx.ALL, 5)
        hbox3.Add(button_clear, 1, wx.EXPAND | wx.ALL, 5)
        # 垂直布局
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox1)
        vbox.AddSpacer(5)
        vbox.Add(hbox2)
        vbox.AddSpacer(5)
        vbox.Add(hbox3)
        panel.SetSizer(vbox)

        # 绑定事件
        self.t2.SetMaxLength(6)
        self.t2.Bind(wx.EVT_TEXT_MAXLEN, self.delag)


app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()
