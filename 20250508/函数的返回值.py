#
def add(*args):
    # 求和
    total = sum(args)

    # 求阶乘
    y = 1
    for i in args:
        y *= i

    # 多个返回值会返回成一个元组
    return total, y


x = add(1, 2, 3, 4)
print(f"和为：{x[0]},阶乘为：{x[1]}")
