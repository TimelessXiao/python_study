# 引入模块
import wx


class MyFrame(wx.Frame):
    # button按钮绑定事件
    def on_click(self, event):
        button_change = wx.MessageDialog(self, "登录成功", "提示", wx.OK)
        text1 = wx.StaticText(self, label="登录成功", pos=(300, 200))
        button_change.ShowModal()

    # 构造器
    def __init__(self):
        # 创建窗体对象
        super().__init__(None, title="wxPython Frame", size=(800, 600))
        # 创建面板
        panel = wx.Panel(self)
        # 创建静态文本（控件）(第一个控件组)
        text = wx.StaticText(panel, label="用户名", pos=(50, 50))
        text_ctrl1 = wx.TextCtrl(panel, pos=(100, 50), size=(100, 50))
        # 密码(第二个控件组)
        text = wx.StaticText(panel, label="密码", pos=(50, 100))
        text_ctrl2 = wx.TextCtrl(panel, pos=(100, 100), size=(100, 50), style=wx.TE_PASSWORD)
        # 创建按钮
        button = wx.Button(panel, label="登录", pos=(100, 150), size=(100, 50))
        button.Bind(wx.EVT_BUTTON, self.on_click, button)


app = wx.App()
myFrame = MyFrame()
myFrame.Show()
app.MainLoop()
