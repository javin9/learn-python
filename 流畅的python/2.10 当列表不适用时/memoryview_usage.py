from array import array

print("=== 内置 array 模块演示 ===")
octets = array('B', range(6))
m1 = memoryview(octets)
print(m1.tolist())
[0, 1, 2, 3, 4, 5]
m2 = m1.cast('B', [2, 3])
print(m2.tolist())
[[0, 1, 2], [3, 4, 5]]
m3 = m1.cast('B', [3, 2])
print(m3.tolist())
[[0, 1], [2, 3], [4, 5]]
m2[1, 1] = 22
m3[1, 1] = 33
print(octets)
array('B', [0, 1, 2, 33, 22, 5])
