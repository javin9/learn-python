# 6.1 流程控制语句
# python是通过换行和缩进 来控制代码的执行
# python的代码不能混淆压缩
mod = True
if mod:
    print('Hello, world!')
else:
    print('Hello, Python!')

a = []
if a:
    print('a is not empty')
else:
    print('a is empty')

# 常量的定义 一般用大写
ACCOUNT = 'javin9'
PWD = '123456'

print('please input account')
user_account = input()
print('please input password')
user_pwd = input()

if (ACCOUNT == user_account and PWD == user_pwd):
    print('success')

else:
    print('fail')

# 6.2 循环控制语句
7


# https://stackoverflow.com/questions/46701063/why-doesnt-python-have-switch-case-update-match-case-syntax-was-added-to-pyt
# https://www.datacamp.com/tutorial/python-switch-case
def f(x):
    return {
        1: 'output for case 1',
        2: 'output for case 2',
        3: 'output for case 3'
    }.get(x, 'default case')


# if else  可以 用 a or b 来代替

# 循环 while for
CONDATION = True

while CONDATION:
    print('Hello, world!')
    CONDATION = False

a = [5, 4, 3, 2, 1]

# 冒泡排序
for i in range(len(a)):
    for j in range(i, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

for i in range(len(a)):
    for j in range(i, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

print(a)

for x in a:
    if (x == 3):
        break
    print(x)

print('end')
for i in range(10):
    print(i)

for i in range(2, 10):
    print(i)

print("递增")
for i in range(2, 10, 2):
    print(i)

print("递减")
for i in range(10, 0, -2):
    print(i)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in range(0, len(a), 2):
    print(a[x])

# name = input('What is your name?')
print(a[0:len(a):2])
