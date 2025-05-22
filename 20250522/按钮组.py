# 引入模块
import wx


# 创建窗口类
class MyFrame(wx.Frame):

    def __init__(self):
        #  创建窗口
        super().__init__(None, title="单选按钮", size=(600, 800))
        panel = wx.Panel(self)

        # 创建单选按钮
        # 按钮组
        str = ["男", "女"]
        a = wx.RadioBox(panel, label="性别", pos=(100, 100), choices=str)


app = wx.App()
myFrame = MyFrame()
myFrame.Show()
app.MainLoop()

1111111
