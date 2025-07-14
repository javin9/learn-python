from collections import deque

import heapq
for i in range(1, 5):
    print(i, end='\n')

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)

obj = {'a': 1, 'b': 2, 'c': 3}
for key in obj.items():
    print(key)

for key, value in obj.items():
    print(key, value)

queue = deque(maxlen=3)
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
print(queue, len(queue))
for i in range(len(queue)):
    print(queue.popleft())

print("-----------------")
# heapq 队
# nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# print(heapq.nlargest(3, nums))
# print(heapq.nsmallest(3, nums))

# 创建一个空列表作为堆
heap = [1, 2, 34, 5, 6, 7, 8, 9, 0]

# 向堆中添加元素
# heapq.heappush(heap, 10)
# heapq.heappush(heap, 20)
# heapq.heappush(heap, 5)

print(heapq.nlargest(3, heap))
"""
1.1.3 保留最后 N 个元素
2.在Python中，enumerate 是一个内置函数，它用于遍历一个可迭代对象（如列表、元组或字符串）时，
  同时获得元素的索引和值。它返回一个枚举对象，该对象生成一个包含索引和值的元组序列。index在前
"""
