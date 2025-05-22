# 封装窗体类
# 引入模块
import time

import wx


# 自定义窗体类
# 创建一个新类 MyFrame，它是 wx.Frame 的子类
class MyFrame(wx.Frame):
    def change_time(self, event):
        str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.text.SetLabelText(str)

    # 这个 self 就表示：当前正在创建的 MyFrame 对象
    def __init__(self):
        # 创建窗体
        # 调用 wx.Frame 的构造函数
        # 原代码 window = wx.Frame(None, title="这是一个窗体", size=(300, 200))
        # 相当于： wx.Frame(None, title="这是一个窗体", size=(300, 200))并实例化这个对象
        super().__init__(None, title="这是一个窗体", size=(300, 200))
        # 创建面板
        panel = wx.Panel(self)
        # 创建静态文本
        self.text = wx.StaticText(panel, label="这是一个静态文本!", pos=(100, 80))
        # 按钮
        button = wx.Button(panel, label="点击改变时间", pos=(100, 100))
        # 事件绑定
        self.Bind(wx.EVT_BUTTON, self.change_time, button)


app = wx.App()
frame = MyFrame()

frame.Show()
app.MainLoop()
