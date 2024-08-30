def yield_test():
    x = 1
    yield x
    yield x + 1
    yield x + 2


yield_test_var = yield_test()
print(type(yield_test_var))
for i in yield_test_var:
    print(i)

s = 'coder'
# print(s[::0]) error

numbers = [n for n in range(3)]
print(numbers)
