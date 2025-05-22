# 断言关键字 assert
num = input("请输入一个整数1：")
if num == "1":
    print("输入的数字正确")
else:
    print("输入的数字不正确")

# 抛出的异常是 AssertionError 它是 Python 中的一种异常，表示程序中某个使用 assert 语句的断言失败了。
assert num == "1", "输入的数字不正确,使用的是assert"
print("输入的数字正确")
