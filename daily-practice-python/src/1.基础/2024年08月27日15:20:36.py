from collections import ChainMap
import re

print("-------ChainMap--------")
a = {"x": 1, "y": 2, "z": 3}
b = {"w": 10, "x": 11, "y": 2}

c = ChainMap(a, b)

print(c)

print("-------update-使用update()方法-------")
d = a.copy()
d.update(b)
print(d)

# **
print("-------**--使用字典解包（Python 3.5+）------")
print({**a, **b})

#
print("-------**--使用|运算符（Python 3.9+）------")
print(a | b)

# 注意事项
# 如果两个字典中有相同的键，后面的字典的值会覆盖前面的字典的值。
# 上述方法都不会修改原始字典 a 和 b，而是创建一个新的合并后的字典。
# 选择适合你的 Python 环境和版本的方法即可。

print("-------**--正则------")
line = 'asdf fjdk; afed, fjek,asdf, foo'
result = re.split(r'[;,\s]\s*', line)
print(result)

print("-------**--fin------")
