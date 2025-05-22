class User:
    name = 'user'

    # 实例方法，他在操作当前的对象
    def set_name(self, name):
        self.name = name

    # 类方法，他在操作类，而不是当前对象
    @classmethod
    def set_name_class(cls, name):
        cls.name = name


user = User()
# 调用实例方法 set_name，并将 'Timeless' 作为参数传入
# 此时 self 的值为 user 实例
user.set_name('Timeless')

# 下面这行代码会报错，因为 set_name 是一个实例方法，不是类方法
# 如果直接通过类调用，则不会自动传入 self 参数，会导致 TypeError
# User.set_name('Timeless')

# 调用类方法 set_name_class，并将 'Timeless' 作为参数传入
User.set_name_class('直接调用类方法')
print(user.name)
print(User.name)


# 静态方法
class Math:
    # 静态方法没有固定的形参
    @staticmethod
    def sum(*args):
        n = 0
        for i in args:
            n += i
        return n


math = Math()
print(math.sum(1, 2, 3, 4, 5))

# 1. 实例方法：
# - 用于操作实例对象。
# - 需要 `self` 参数，自动传入当前实例。
# - 可以访问/修改实例属性和类属性（通过 self）。
# - 绑定在实例上，调用时会传入实例的内存地址。

# 2. 类方法：
# - 用于操作类本身。
# - 需要 `cls` 参数，自动传入当前类。
# - 可以访问/修改类属性，不能访问实例属性。
# - 绑定在类上，调用时传入类的内存地址。

# 3. 静态方法：
# - 通常用于执行与类相关但不依赖类或实例状态的功能。
# - 不需要 `self` 或 `cls`，没有自动传参。
# - 不能访问类属性或实例属性（除非手动传入）。
# - 不绑定任何内存对象，仅是类中的普通函数。
