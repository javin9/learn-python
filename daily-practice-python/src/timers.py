import os
import pdb
import sys
import time


class Timers():

    def __init__(self, start_time) -> None:
        self.start_time = start_time if start_time is not None else time.time()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        print(f"Time taken: {self.end_time - self.start_time} seconds")
        return True


def debugger():
    debug = eval(os.environ.get('DEBUG', 'False'))
    if debug:
        pdb.Pdb().set_trace(sys._getframe().f_back)


def fun():
    os.environ['DEBUG'] = 'True'
    debugger()
    print("Hello")


def duplicate(iterable, reverse=False):
    result = []
    if reverse:
        iterable = reversed(iterable)
    for item in iterable:
        if item not in result:
            result.append(item)

    return result


def chain_all(*args):
    result = []
    for iterable in args:
        result = result + iterable
    return result


def merge_obj(*args):
    result = {}
    for obj in args:
        result = {**result, **obj}
    return result


if __name__ == "__main__":
    result = duplicate([2, 1, 3, 4, 5, 1, 2, 3, 4, 5], reverse=True)
    result1 = chain_all([1, 2, 3], [4, 5, 6], [7, 8, 9])
    print(result, end="\n")
    print(result1, end="\n")
    result2 = merge_obj({'a': 1, 'b': 2}, {'c': 3, 'd': 4})
    print(result2, end="\n")
    # fun()
    with Timers(time.time()) as timer:
        time.sleep(2)
