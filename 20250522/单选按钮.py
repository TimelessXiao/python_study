# 引入模块
import wx


# 创建窗口类
class MyFrame(wx.Frame):

    def __init__(self):
        #  创建窗口
        super().__init__(self, None, title="单选按钮", size=(400, 300))
        panel = wx.Panel(self)

        # 创建单选按钮
        radio1 = wx.RadioButton(panel, label="男", style=wx.RB_GROUP)
        radio2 = wx.RadioButton(panel, label="女")

        # 水平布局
        vbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox.Add(radio1, 0, wx.ALL, 5)
        vbox.Add(radio2, 0, wx.ALL, 5)


app = wx.App()
myFrame = MyFrame()
myFrame.Show()
app.MainLoop()
