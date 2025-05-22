class User:

    # 有参构造
    def __init__(self, name, age):
        # 添加实例属性
        self.name = name
        self.age = age


user = User('Timeless', 18)
print(user.name)
print(user.age)


# 使用有参构造方法后，默认的无参构造消失，此时调用无参构造方法会报错
# user = User()


class UserWCan:

    # 有参构造
    def __init__(self, name, age):
        # 添加实例属性
        self.name = name
        self.age = age

    # 无参构造方法会覆盖有参构造方法，一个类里面只能有一个构造方法
    def __init__(self):
        print('无参构造方法')


UserWCan()


# 报错
# user = UserWCan('Timeless', 18)


# 析构方法
class UserD:

    # 有参构造
    def __init__(self, name, age):
        # 添加实例属性
        self.name = name
        self.age = age

    # 析构方法
    def __del__(self):
        print('析构方法自动被调用，对象被销毁时会自动调用')


user = UserD('Timeless', 18)

# 析构方法会自动调用，无需手动调用
user = UserD('Timeless', 18)
print('对象创建完毕')
del user
print('手动删除对象之后')
