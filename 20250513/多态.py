class Fu:
    def fun(self):
        print('这是一个父类的方法')


class Son(Fu):
    def fun(self):
        print('这是一个子类的方法')


# obj是一个不确定的对象，可以是父类对象，也可以是子类对象，通用
def duo_tai(obj):
    return obj.fun()


# 原始调用
fu = Fu()
fu.fun()
son = Son()
son.fun()

# 多态的调用
duo_tai(fu)

duo_tai(son)
