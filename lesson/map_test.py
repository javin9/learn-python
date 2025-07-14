def square(x):
    return x * x


arr = [1, 2, 3, 4, 5]

result = map(square, arr)

print(list(result))

result2 = map(lambda x: x * x, arr)

print(list(result2))


def fileter_callback(x):
    return x > 3


print(list(filter(fileter_callback, arr)))
