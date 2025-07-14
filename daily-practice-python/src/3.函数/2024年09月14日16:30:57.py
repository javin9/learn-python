def test(*args, **kargs):
    print(args)
    print(kargs)


test(1, 2, 3, 4, 5, name=1, age=2)


def a(x, *args, y):
    pass


def b(x, *args, y, **kwargs):
    pass
