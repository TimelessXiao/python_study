class Fu1:
    def fun1(self):
        print('父类1：方法1')

    def fun2(self):
        print('父类1：方法2')

    def test(self):
        print('父类1：方法3')


class Fu2:
    def fun1(self):
        print('父类2：方法1')

    def fun3(self):
        print('父类2：方法2')


class Son(Fu2, Fu1):
    def test(self):
        print('子类：方法1')


# 父类1和父类2都有方法1，直接执行参数第一个父类中的方法1
# 子类和父类1和父类2都有方法3，执行子类方法3
son = Son()
son.fun1()
son.test()
