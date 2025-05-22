# 引入模块
import wx


# 创建窗口类
class MyFrame(wx.Frame):

    def __init__(self):
        #  创建窗口
        super().__init__(None, title="复选框", size=(300, 300))
        #  创建面板
        panel = wx.Panel(self)

        #  创建复选框
        cb1 = wx.CheckBox(panel, label="复选框1", pos=(100, 100))
        #  默认勾选
        cb1.SetValue(True)
        cb2 = wx.CheckBox(panel, label="复选框2", pos=(100, 200))
        cb3 = wx.CheckBox(panel, label="复选框3", pos=(100, 300))

        # 绑定按钮事件，获取值
        self.Bind(wx.EVT_CHECKBOX, self.check_box_click)
        # 添加布局，水平布局
        cbox = wx.BoxSizer(wx.HORIZONTAL)
        cbox.Add(cb1)
        cbox.Add(cb2)
        cbox.Add(cb3)
        panel.SetSizer(cbox)

        # 通过事件获取值

    def check_box_click(self, event):
        obj = event.GetEventObject()
        print(f"选中的复选框是：{obj.GetLabel()},状态是：{obj.IsChecked()}")


app = wx.App()
myFrame = MyFrame()
myFrame.Show()
app.MainLoop()
