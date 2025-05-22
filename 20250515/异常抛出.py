name = input('请输入一个名字：')
# 设置关键词禁用 '毛主席'
if name == '毛主席':
    # 报错
    # IndexError  是 Python 中的一种常见错误，意思是索引超出范围
    # raise IndexError #  手动抛出错误
    raise Exception('您输入的姓名敏感，请重新输入')
else:
    print('欢迎您：%s' % name)
