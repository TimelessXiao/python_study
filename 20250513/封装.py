class User:
    __name = 'user'

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def to_string(self):
        print(f"name:{self.__name}\n")


user = User()
user.set_name('Timeless')
print(user.get_name())
user.to_string()
