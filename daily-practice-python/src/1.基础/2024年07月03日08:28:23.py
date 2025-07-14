from collections import deque, OrderedDict
import json

queue = deque(maxlen=3)

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

print("--------OrderedDict---------")
dic_test = OrderedDict()
dic_test.setdefault("a", 1)
dic_test.setdefault("c", 2)
dic_test.setdefault("b", 3)

print(dic_test)
print(json.dumps(dic_test))
print(type(json.dumps(dic_test)), '----------')
json.loads(json.dumps(dic_test))

for key, value in dic_test.items():
    print(key, value)

print("-------dic 可以 用min和max----------")
dic = {1: "a", 6: "b", 3: "c"}
print(min(dic))
print(max(dic))

print("-------字典key和value交换----------")
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
zip(prices.values(), prices.keys())
print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))

print("--------a-b---------")
a = {'x': 1, 'y': 2, 'z': 3}

b = {'w': 10, 'x': 11, 'y': 2}
print(a.keys() - b.keys())

print(a.keys(), b.keys(), a.keys() & b.keys())
result = a.keys() & b.keys()
print(type(result))
a, *reset = result
print(a)

print("--------列表推导式---------")
a_list = [x * x for x in range(10)]
print(a_list)

print("--------列表对导师---------")
fresh_fruit = [' banana', ' loganberry ', 'passion fruit ']
str_list = [weapon.strip() for weapon in fresh_fruit]
print(str_list)

print("--------列表推导式---------")
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [item2 for item1 in vec for item2 in item1]
print(result)

#
print("--------列表推导式---------")
arr = [-1, -4, 6, 7.5, -2.3, 9, -11]
result = [item for item in arr if item > 0]
print(result)

# 查找列表中最大元素的所有位置。
print("--------查找列表中最大元素的所有位---------")
arr = [10, 2, 3, 4, 5, 10, 10, 9, 2, 4, 10, 8, 2, 2, 9, 7, 6, 2, 5, 6]
max_value = max(arr)
result = [index for index, item in enumerate(arr) if item == max_value]
print(result)

print("--------字典推导式---------")
b = {'w': 10, 'x': 11, 'y': 2}
new_obj = {key: value for key, value in b.items() if value > 5}
new_obj2 = {key: b[key] for key in b.keys() - {'x'}}
print(new_obj)
print(new_obj2)

print("--------集合推导式---------")

a = [1, 5, 2, 1, 9, 1, 5, 10]


def remove_duplicates(arr):
    return list(set(arr))


print(remove_duplicates(a))


def remove_duplicates2(arr):
    cache = []
    for item in arr:
        if item not in cache:
            cache.append(item)
    return cache


print(remove_duplicates2(a))


def remove_duplicates3(arr):
    cache = []
    for item in arr:
        if item not in cache:
            yield item
            cache.append(item)


print(list(remove_duplicates3(a)))

a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

# def remove_duplicates4(arr):
#     cache = []
#     for item in arr:
#         if item not
"""总结
1.列表推导式，字典推导式，集合推导式
2.推导式的使用 for if else
3.zip函数的使用，可以交换key和value
4.min，max可以用于字典，第二个参数key 为函数
5.OrderedDict的使用
"""
