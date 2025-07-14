a = {
    'x': 1,
    'y': 2,
    'z': 3,
}
b = {'w': 10, 'x': 11, 'y': 2}

common = a.keys() & b.keys()  # 返回一个集合，包含两个字典中都有的键
print(common)
for item in common:
    print(item)

distance = a.keys() - b.keys()  # 返回一个集合，包含所有在 a 中有但 b 中没有的键
print(distance)

#

new_value = {key: a[key] for key in a.keys() - {'z'}}  # 列表推导式
print(new_value)

*new_value2, z = a
print(new_value2)

c = a.items() & b.items()  # 返回一个集合，包含两个字典中都有的键值对
print(c)

print("-----------------")
a = [1, 5, 2, 1, 9, 1, 5, 10]


def deduce(items):
    result = set()
    for item in items:
        if item not in result:
            yield item
            result.add(item)


result = list(deduce(a))
print(result)


def deduce_dic(items, cb=None):
    result = set()
    for item in items:
        value = item if cb is None else cb(item)
        if value not in result:
            yield item
            result.add(value)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(deduce_dic(a, lambda item: (item['x'], item['y']))))
"""_summary_
1.dic的keys和items返回的都是集合，可以进行集合操作
2.去重就用set
"""
