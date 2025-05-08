# 单继承
class Person:
    def set_name(self, name, age):
        self.__name = name
        self.age = age

    def get_name(self):
        return self.__name

    def to_string(self):
        return f"name: {self.__name}"


# 继承父类User
class Student(Person):
    # pass是一个占位符，处理缩进问题
    pass


student = Student()
student.set_name('Timeless', 18)
print(student.to_string())
print(student.age)

print("--------")


# 继承父类User，同时还有自己的东西
class Teacher(Person):
    def set_sex(self, sex):
        self.__sex = sex

    def get_sex(self):
        return self.__sex

    # 子类重写父类的方法
    def to_string(self):
        # 私有属性必须通过方法来获取，公开的是直接访问
        return f"name: {self.get_name()},age: {self.age}, sex: {self.get_sex()}"


teacher = Teacher()
teacher.set_name('Teacher', 18)
teacher.set_sex('man')
print(teacher.get_sex())
print(teacher.to_string())
