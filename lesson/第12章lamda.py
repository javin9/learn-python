# # 匿名函数
# lambda x: x * x

# # f(2)  # 输出: 4
# sum = lambda a, b: a + b
# print(sum(5, 3))  # 输出: 8

from functools import reduce
import time

result = map(lambda x: x * 2, [1, 2, 3, 4])
print(result, list(result))  # 输出: [2, 4, 6, 8]

# 三元表达式
# 条件为真时的结果 if 条件判断 else 条件为假时的结果
x = 1
y = 2
r = x if x > y else y


# result2 = reduce(lambda x, y: x + y, [1, 2, 3, 4])
def hanlde(x):
    return x * x if x % 2 == 0 else x + 1
    # if x % 2 == 0:
    #     return x * x
    # else:
    #     return x + 1


result2 = map(hanlde, [1, 2, 3, 4])
print(list(result2))  # 输出: [2, 4, 4, 16]

# from functools import reduce
result3 = reduce(lambda x, y: x + y, [1, 2, 3, 4], 100)
print(result3)  # 输出: 110

result4 = filter(lambda x: x % 2 == 0, [1, 2, 3, 4])
print(list(result4))  # 输出: [2, 4]

# 参数和后面的参数个数一样
result5 = map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])
print(list(result5))  # 输出: [5, 7, 9]

char_list = ['a', 'b', 'c', 'A', "B", 'd']

result6 = filter(lambda x: ord(x) < 97, char_list)
print(list(result6))  # 输出: ['A', 'B']

# print(time.time())
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(formatted_time)  # 输出类似于 "2024-03-18 20:51:27"

time_string = "2024-03-18 20:51:27"
time_tuple = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
print(time_tuple)  # 输出类似于 time.struct_time(tm_year=2024, tm_mon=3, ...)

# strfime 将时间转换成字符串
# strptime 将字符串转换成时间
# time.localtime() 获取当前时间


def my_decorator(func):

    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)  # 调用原始函数
        print("Something is happening after the function is called.")
        return result

    return wrapper


# 使用装饰器
@my_decorator
def say_hello(name):
    print("Hello!", name)


# 调用函数
say_hello('world')  # 输出:
