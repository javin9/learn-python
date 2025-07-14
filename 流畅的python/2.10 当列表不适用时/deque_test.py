from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)  # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)

dq.appendleft(-1)
print(dq)  # deque([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8], maxlen=10)

dq.append(1)
print(dq)  # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 1], maxlen=10)

dq.extend([11, 22, 33])
print(dq)  # deque([2, 3, 4, 5, 6, 7, 8, 1, 11, 22], maxlen=10)

dq.extendleft([10, 20, 30, 40])
print(dq)  # deque([40, 30, 20, 10, 2, 3, 4, 5, 6, 7], maxlen=10)

# 将 deque 转换为 list
print(list(dq))
