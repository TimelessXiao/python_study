class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 两个实例对象的年龄相加，返回值
    def __add__(self, other):
        return self.age + other.age

    # 两个实例对象的年龄相减，返回值
    def __sub__(self, other):
        return self.age - other.age


person = Person('张三', 18)
person1 = Person('李四', 20)

# 运算符重载，相当于person.add(person1)
print(person + person1)
print(person - person1)
