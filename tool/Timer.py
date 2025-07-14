import time


class Timer(object):
    """
    计时器，对于需要计时的代码进行with操作：
    with Timer() as timer:
        ...
        ...
    print(timer.cost)
    ...
    """

    def __init__(self, start=None):
        if start is None:
            self.start = time.time()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = time.time()
        self.cost = self.stop - self.start
        return exc_type is None


class Mytimer():

    def __init__(self, startTime=None):
        if startTime is None:
            self.startTime = time.time()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.endTime = time.time()
        self.cost = self.endTime - self.startTime
        return exc_type is None
        # return self


if __name__ == "__main__":
    with Mytimer() as my_timer:
        print("开始休息3秒")
        time.sleep(3)
        print("开始休息3秒结束")
    print(my_timer.cost)
"""
with的用法
上下文管理器
https://zhuanlan.zhihu.com/p/183779277
"""
