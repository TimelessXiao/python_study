# 全局变量
a = 1
b = 2


# 方法体中可以访问全局变量，方法体中的局部变量不能在方法外访问
def add(c):
    # 方法体中可以访问全局变量最好不要修改，最好使用global关键字改变a的作用域
    global a
    a = 3
    d = 4
    return a + b + c + d


print(a)
print(add(3))


# 求阶乘
def fun(n):
    if n == 1:
        return 1
    else:
        return n * fun(n - 1)


print(fun(5))
