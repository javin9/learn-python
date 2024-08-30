def cur_func():
    a = 1

    def func():
        print(a)

    return func


ff = cur_func()
ff()
ff()
ff()
ff()


def make_multiplier_of(n):
    # 这是外围函数
    a = 1

    def multiplier(x):
        nonlocal a
        a = a + 1
        # 这是嵌套函数，它将成为一个闭包
        return x * n * a

    return multiplier  # 返回嵌套函数


# 创建一个“乘以3”的函数
times3 = make_multiplier_of(3)

# 创建一个“乘以5”的函数
times5 = make_multiplier_of(5)

# 测试这些函数
print(times3(9))  # 输出: 27
print(times5(3))  # 输出: 15
print(times3(times5(2)))  # 输出: 30


def make_counter():
    count = 0

    def counter():
        nonlocal count  # 声明count不是局部变量
        count += 1
        return count

    return counter


counter1 = make_counter()
print(counter1())  # 输出: 1
print(counter1())  # 输出: 2


def f1():
    a = 10

    def f2():
        nonlocal a
        a = 20
        print(a)

    return f2
