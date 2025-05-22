str1 = input("请输入被除数")
str2 = input("请输入除数")

# ZeroDivisionError 是 Python 中的一种运行时错误，表示除数为零的异常情况
# print(int(str1) / int(str2))

# ValueError 是 Python 中的一个内置异常，表示你传给函数或操作的参数虽然类型正确，但值不合适。这类错误常出现在类型转换、数学函数、解包操作等场景中。
# print(int("aaa"))

# 捕获异常，单个
try:
    print(int(str1) / int(str2))
except ZeroDivisionError:
    print("出错了，捕获ValueError")

# 捕获异常，多个
try:
    print(int(str1) / int(str2))
except (ZeroDivisionError, ValueError):
    print("出错了，捕获ValueError")

# 捕获异常，多个
try:
    print(int(str1) / int(str2))
except ValueError:
    print("整数类型转换失败")
except  ZeroDivisionError:
    print("除数不能为0")

# 输出捕获的异常
try:
    print(int(str1) / int(str2))
except Exception as e:11
    print(e)

# try-except-else
# try(可能出错的代码)-except(可以有多个捕获)-else(没有出错的情况下执行)-finally(不管有没有异常都会执行)
try:
    print(int(str1) / int(str2))
except Exception as e:
    print(e)
else:
    print("没有异常")
finally:
    print("不管有没有异常，都会执行")
