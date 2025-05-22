# 引入模块
import time

import wx

# 创建对象
app = wx.App()

# 创建窗口
window = wx.Frame(None, title="wxPython Frame", size=(800, 600))

# 创建面板
panel = wx.Panel(window)
text = wx.StaticText(panel, label="当前时间：", pos=(100, 50))
button = wx.Button(panel, label="点击我修改时间", pos=(100, 100), size=(100, 50))


def change_time(event):
    str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    text.SetLabelText(str)


# 绑定事件
window.Bind(wx.EVT_BUTTON, change_time, button)

# 显示窗口
window.Show(True)
app.MainLoop()
