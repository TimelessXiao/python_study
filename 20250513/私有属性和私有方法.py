class User:
    # 私有属性，使用两个下划线开头
    __name = 'user'

    @classmethod
    def set_name_class(cls, name):
        cls.__name = name

    @classmethod
    def get_name_class(cls):
        return cls.__name

    @classmethod
    def __private_method(cls):
        print('这是一个私有方法，外部不能直接调用，可以在其它的公开方法中被调用')

    @classmethod
    def public_method(cls):
        cls.__private_method()


# 私有属性不能在外部访问，会报错
# print(User.name)

User.set_name_class('私有属性的名字被调用')

print(User.get_name_class())

# 私有方法不能被调用，会报错
# User.private_method()

User.public_method()
