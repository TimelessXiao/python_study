# 导入wx模块 wxPython
import wx

# 创建窗体应用
app = wx.App()
# 窗体标题以及宽高（宽300px，高200px）
window = wx.Frame(None, title="wxPython Frame", size=(300, 200))
# 在上一个窗口中创建一个面板，默认的大小就是窗口的大小
panel = wx.Panel(window)
# 在面板中创建一个静态文本，文本内容是"Hello World"，位置为（100，50）距离窗体的左上角100px，50px
label = wx.StaticText(panel, label="Hello World", pos=(100, 50))
#  显示窗体
window.Show(True)
# 窗体应用循环显示
app.MainLoop()
