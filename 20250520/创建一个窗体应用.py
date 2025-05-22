# 引入依赖
import wx

# 创建窗体应用对象
app = wx.App()

# 创建窗口
# Wx.Frame (parent, id, title, pos, size, style, name)
# parent: 父窗口
# id: 窗口ID
# title: 窗口标题
# pos: 窗口位置
# size: 窗口大小
# style: 窗口样式
# name: 窗口名称
window = wx.Frame(None, title="wxPython Frame", size=(300, 200))
window2 = wx.Frame(None, title="这是第二个窗口", size=(100, 100), pos=(200, 500))

# 显示窗口(只会显示一下，显示后瞬间退出)
window.Show(True)
window2.Show(True)
# 循环显示窗口（一直显示窗口）
app.MainLoop()
