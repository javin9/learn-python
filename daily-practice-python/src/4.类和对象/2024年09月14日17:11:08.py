# 改变对象的字符串显示 __str__ 和 __repr__
import time


class Pair:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


p = Pair(3, "4")
print(p)

print("我是你的{0!r}".format(p))  # 我是你的Pair(3, '4')
print("我是你的{0}".format(p))  # 我是你的(3, 4)
print(p.x)


class Timer:

    def __init__(self, start_time) -> None:
        self.start_time = start_time

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        print(f"Time taken: {self.end_time - self.start_time} seconds")
        return True


with Timer(time.time()) as t:
    time.sleep(2)
