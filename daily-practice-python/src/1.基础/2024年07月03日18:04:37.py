from json import JSONEncoder
import json


class MyDefined(object):

    def __init__(self):
        self.name = "yoyo"
        self.age = 18

    def __repr__(self):
        return '111-name={}&age={}'.format(self.name, self.age)


def new_default(self, obj):
    if isinstance(obj, MyDefined):
        return str(obj)
    else:
        return JSONEncoder.default(self, obj)


JSONEncoder.default = new_default

a = MyDefined()

print(json.dumps(a))

print("-----------------")
c = [(1, 1), (2, 3)]
print((2, 3) in c)

a = [{'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
b = [(item['x'], item['y']) for item in a]
print(list(set(b)))
# print(list(set(a)))

# def remove_duplicate(arr):
#     return list(set(arr))


def remove_duplicate(arr):
    cache = []
    for item in arr:
        item_tuple = item if item is None else (item['x'], item['y'])
        if item_tuple not in cache:
            # yield item_tuple
            cache.append(item_tuple)
    return cache


result = remove_duplicate(a)
print(result)

# def dedupe(items, key=None):
#     seen = set()
#     for item in items:
#         val = item if key is None else key(item)
#         if val not in seen:
#             yield item
#             seen.add(val)
""" 总结
   1. 猴子补丁的使用。
   2.__repr__方法的使用
   3.set([]) 去重的内容不限于基本类型，也可以是元组等
"""
