# 引入模块
import wx

# 创建对象
app = wx.App()

# 创建一个窗口
window = wx.Frame(None, title="wxPython Frame", size=(500, 500))

# 在窗口中创建一个面板
panel = wx.Panel(window, size=(100, 100))
panel1 = wx.Panel(window, size=(200, 200), pos=(200, 200))

# 在面板中添加内容(静态文本(子控件))
# Wx.StaticText(parent, id, label, position, size, style)
# parent: 父控件
# id: 控件的ID
# label: 显示的文本
# position: 静态文本的位置
# size: 静态文本的大小
# style: 静态文本的样式
label = wx.StaticText(panel, label="Hello World", pos=(0, 20))
label1 = wx.StaticText(panel1, label="Hello World")

# 显示窗口
window.Show(True)
app.MainLoop()
