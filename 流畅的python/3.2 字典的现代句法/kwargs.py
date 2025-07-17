def dump(**kwargs):
    print(kwargs)


dump(**{'x': 1}, y=2, **{'z': 3})

d1 = {'a': 1, 'b': 2}
d2 = {'a': 222, 'b': 7089, 'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

# 合并字典，不改变引用，而是创建新的字典
print(d1 | d2 | d3)

d1 |= d2
# 不改变引用，而是修改d1
print(d1)
