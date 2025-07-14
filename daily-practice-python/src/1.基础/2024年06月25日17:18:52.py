str_1 = "hello"
a, b, _, _, _ = str_1

print(a, b)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212',
          "123-456-7890")
name, email, *phone_numbers = record
print(phone_numbers, type(phone_numbers))

name, email, *phone_numbers, last = record

print(phone_numbers, type(phone_numbers))


def sum(arr):
    head, *tail = arr
    return head + sum(tail) if tail else head


print(sum([1, 2]))
"""_summary_
  1.这个表达式是一个Python中的条件表达式（也称为三元运算符），。
  2.分解，结构
"""
