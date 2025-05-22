class User:
    # 类属性
    name = 'user'

    def change_name(self, change_name):
        #  实例属性
        self.name = change_name


# 现在调用的是类属性
user = User()
print(user.name)
print(User.name)

print("----------")
# 现在调用的是实例属性
user.change_name('TimelessXiao')
print(user.name)
# 现在调用的是类属性，类属性的值没有被改变
print(User.name)

print("----------")
# 修改类属性
User.name = '修改类属性的值'
print(User.name)
print(user.name)

print("----------")
# 动态添加实例属性,没有属性可以添加属性
user.birthday = '2003-01-05'
print(user.birthday)
