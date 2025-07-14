# sorted(iterable, key=None, reverse=False)

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(sorted(numbers, reverse=True))
# 输出: [9, 6, 5, 4, 3, 2, 1, 1]

# 对于元组列表，sorted() 默认按第一个元素排序，如果第一个元素相同，则按第二个元素排序，以此类推
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

# 输出:
# BRA/CE342567
# ESP/XDA205856
# USA/31195855

# 使用 key 参数进行自定义排序.key 参数可以接受一个函数，用于指定排序的依据
words = ['python', 'java', 'javascript', 'go', 'rust']
print(sorted(words,
             key=len))  # 输出: ['go', 'java', 'rust', 'python', 'javascript']

numbers = [-5, -1, 0, 1, 3, -2]
print(sorted(numbers, key=abs))  # 输出: [0, -1, 1, -2, 3, -5]

# 按第二个元素排序
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
print(sorted(
    students,
    key=lambda x: x[1]))  # 输出: [('Charlie', 78), ('Alice', 85), ('Bob', 92)]

# 按第一个元素的长度排序
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
print(sorted(traveler_ids, key=lambda x: len(x[0]))
      )  # 输出: [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
