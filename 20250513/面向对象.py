class Person:
    # 类属性，在类中定义的属性，所有实例共享
    name = 'Timeless'
    sex = 'woman'
    age = 18

    def hobby(self, other, name):
        print('吃饭')
        print('睡觉')
        print('打游戏')
        print(f'{other}')
        # self 是类方法中的第一个参数，它代表类的实例本身，用于访问实例的属性和方法
        # 实例属性，在方法内部对属性进行操作
        self.name = name
        print(self)


# 调用对象
person = Person()
# 打印内存地址
print(person)
# 打印对象属性
print(person.name)
print(person.sex)
print(person.age)
# 打印对象方法,打印self时是对象的内存地址
person.hobby('打豆豆', '名字已经改变')
print(person.name)
