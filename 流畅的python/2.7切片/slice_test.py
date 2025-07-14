# 基本用法
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 使用 slice 对象
# [start:stop:step]
s1 = slice(2, 8, 2)  # 从索引2开始，到索引8结束（不包含），步长为2
print(data[s1])  # 输出: [2, 4, 6]

# 等价于标准切片语法
print(data[2:8:2])  # 输出: [2, 4, 6]

# 只有 stop 参数
s2 = slice(5)  # 从开始到索引5（不包含）
print(data[s2])  # 输出: [0, 1, 2, 3, 4]

# 等价于
print(data[:5])  # 输出: [0, 1, 2, 3, 4]

s = 'abcdefg'
print(s[::-2])  # geca

r = range(10)  # 创建一个 range 对象
# 将 range 类型转换成 list 类型，使用 list() 函数
print(type(r))
#
