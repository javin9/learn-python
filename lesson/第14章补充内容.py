import copy
from dataclasses import dataclass


def handle_case1():
    return "Case 1 handled"


def handle_case2():
    return "Case 2 handled"


def handle_case3():
    return "Case 3 handled"


def default_case():
    return "No case matched"


switch_dict = {1: handle_case1, 2: handle_case2, 3: handle_case3}


# get 第二个参数是默认值
def switch(case):
    return switch_dict.get(case, default_case)()


# 使用
case_number = 2
result = switch(case_number)
print(result)  # 输出: Case 2 handled

# 列表推导式

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 不带条件的列表推导式
b = [i * i for i in a]
print(b)  # 输出: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 带条件的列表推导式
c = [i**2 for i in a if i % 2 == 0]
print(c)  # 输出: [4, 16, 36, 64, 100]

book = {
    "name": "Python",
    "price": 99,
}

keys = [key for key in book]
print(keys)  # 输出: ["name", "price"]
keys = [item for item in book.items()]
print(keys)  # 输出: [('name', 'Python'), ('price', 99)]
keys = [key for key, value in book.items()]
print(keys)  # 输出: ['name', 'price']

# 可迭代对象 iterable
# 迭代器 iterator
# 1. 列表
# 2. 元组
# 3. 字符串
# 4. 字典
# 5. 集合


# 实现可迭代
class BookCollention:

    def __init__(self):
        self.data = ["Python", "Java", "C++", "Go"]
        # self.index = 0

    def __iter__(self):
        return iter(self.data)

    def __next__(self):
        return next(self.data)


book_collention = [key for key in BookCollention()]
print(book_collention)  # 输出: ['Python', 'Java', 'C++', 'Go']

# 深拷贝
copy.deepcopy(book_collention)

# 浅拷贝
copy.copy(book_collention)


# 生成器
def gen(x):
    for i in range(x):
        yield i  # 生成器 yield 返回值，并且不退出循环


ll = gen(10)
print(list(ll), type(ll))  # 输出: <generator object gen at 0x7f8e3c3e3d60>

next(gen(10))  # 输出: 0
next(gen(10))  # 输出: 1
next(gen(10))  # 输出: 2
next(gen(10))  # 输出: 3

# 变量拼接
a = 23
print(f"有一个值啊，喂喂喂{a}")
print("有一个值啊，喂喂喂{}".format(a))

# dataclass 装饰器
# from dataclasses import dataclass


# 语法糖
@dataclass
class Student:
    name: str
    age: int

    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    def showName(self):
        print(self.name, self.age)


Student("javin", 18).showName()  # 输出: javin 18
