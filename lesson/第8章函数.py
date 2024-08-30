print(round(9.236243, 2))  # 9.24
print(round(9.233243, 2))  # 9.23

# 查看 round 函数的帮助文档
# help(round)


def user_info():
    return 'name', 18  # 返回多个值


result = user_info()  # ('name', 18)
print(result[0], result[1])  # ('name', 18)

# 解包 建议这种方式
name, age = user_info()  # 解包

# 序列解包，链式赋值
a, b, c = 1, 2, 3

# 序列解包
d = 4, 5, 6, 7
print(d, type(d))  # (4, 5, 6, 7) <class 'tuple'>
e, f, g, h = d

# 参数
# *args 接收元组
# **kwargs 接收字典
# *args 必须在 **kwargs 前面
# 任意制定参数 关键字参数


def test(x, y):
    print(x)
    print(y)


test(1, 2)  # 1 2
test(y=2, x=1)  # 1 2  关键字参数

# 默认参数
print("-------默认参数----------")


def print_student_info(name, age=20, collage="清华大学"):
    print("-----------------")
    print('name:', name)
    print('age:' + str(age))
    print('collage:', collage)
    print("我叫{},今年{}了，我学校{}".format(name, age, collage))


print_student_info('石敢当', 18, '清华大学')  # 位置参数
print_student_info('巨无霸', 18)  # 默认参数

# 可变参数
print("--------可变参数---------")


def test2(*args):
    print(args)


test2(1, 2, 3, 4, 5, 6, 7, 8, 9)  # (1, 2, 3, 4, 5, 6, 7, 8, 9)

a = (1, 2, 3)

test2(*a)  # (1, 2, 3)
test2(a)  # ((1, 2, 3), )


def test3(x, y, *args):
    print("-----------------")
    print(x)
    print(y)
    print(args)


test3(1, 2, 3, 4, 5, 6, 7, 8, 9)  # 1 2 (3, 4, 5, 6, 7, 8, 9)


def sqs(*nums):
    sum = 0
    for x in nums:
        sum += x**2
    return sum


result = sqs(1, 2, 3, 4, 5)
print(result)

# 可变参数 可以什么都不传=

print("--------kwargs关键字参数---------")


def kwargsTest(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


kwargsTest(name='石敢当', age=18, collage='清华大学')

print("--------scope_test---------")


def scope_test():
    a = 1
    if a:
        cc = 2
    print(cc)  # 在函数内部定义的变量（包括在 if 语句或循环内部定义的变量）在整个函数内部都是可见的


# cc 是在 if a: 块内部定义的，但是它在 scope_test
# 函数的整个范围内都是可见的。因此，你可以在函数的任何地方访问 cc，包括 print(cc) 语句。
scope_test()
print("--------global---------")
