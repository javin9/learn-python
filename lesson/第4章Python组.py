# @Time : 2024/3/7 20:43
# @Author : javin9
# @Email : 1330361087@qq.com
# @Time : 2024/3/7 19:23
# @Author : javin9
# @Email : 1330361087@qq.com

arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
print(arr[1:8:4])

print(ord('w'))
# 序列 str,list,tuple
# 有序，可以通过下标索引访问  list[0]，支持切片
# 可重复
# 支持的操作 len,max,min,not in ,in
# 字符串 "hello world"
# 列表 [1,2,3,4,5,6,7,8,9,10]
# 元组 (1,2,3,4,5,6,7,8,9,10)
# 元祖 (1,)  # 只有一个元素的元祖,必须要有逗号,()表示数学运算

# 集合 set,dict
# 无序，不可知通过下标访问，不支持切片
# 不重复
# 支持的操作 len,max,min,not in ,in
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(1 in s1)
print(11 not in s1)
print(len(s1))
print(max(s1))  # 10
print(min(s1))  # 1
print({1, 2, 3, 4, 5, 6, 7} - {3, 4})  # 求两个集合的差集 {1, 2, 5, 6, 7}
print({1, 2, 3, 4, 5, 6, 7} & {3, 4})  # 交集 {3, 4}
print({1, 2, 3, 4, 5, 6, 7} | {3, 4})  # 并集 {1, 2, 3, 4, 5, 6, 7}

print(type(set()))  # <class 'set'> # 空集合
print(type({}))  # <class 'dict'>
print(dict())  # {}
print({1: 1, "a": 2})

# 字典的key是不可变的
# python 变量没有类型，什么都可以给他，所以写的时候不需要 let，const，var 这些关键字 int
# python 变量的类型是根据值来确定的
# 值类型 不可以改变 int float str tuple
# 引用类型 可以改变 list dict set

a = (1, 2, ['a', 'b'])
a[2][0] = 'c'  # 可以改变
print(a)

# 判空操作
# if not a:
#     print("a is empty")

user = {"name": "javin", "age": 18}
name_check = "javin"

# if user.get('name') == name_check:
#     print("name_check in user")
# else:
#     print("name_check not in user")

# bb=(1,3,3,4,5,6,7,8,9,10)
# bb[2]=23
# print(bb) # 元祖不支持修改 TypeError: 'tuple' object does not support item assignment
