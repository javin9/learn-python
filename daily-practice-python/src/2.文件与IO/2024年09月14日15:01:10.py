# 5.6 字符串的I/O操作
import io
import json

s = io.StringIO()
s.write('Hello World\n')
print('This is a test', file=s)

my_dict = {'a': 1, 'b': 2, 'c': 3}
my_iter = iter(my_dict)

for k in my_dict.items():
    print(k)
