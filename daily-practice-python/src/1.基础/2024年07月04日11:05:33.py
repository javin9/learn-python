import os


def dedupe(items, key=None):
    seen = []
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.append(val)


def dedupe2(items, key=None):
    seen = []
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.append(val)


filename = os.path.abspath(
    os.path.join(os.getcwd(), "./daily-practice-python/src/a.txt"))


def printLine():
    with open(filename, "r") as f:
        print(f)
        for line in f:
            print(line, end='')


def printLine_duplicate():
    with open(filename, "r") as f:
        print(f)
        for line in dedupe(f):
            print(line, end='')


if __name__ == '__main__':
    printLine()
    printLine_duplicate()
"""_summary_
  1.yield的使用
  2.os.path.abspath()的使用，os.path.join()的使用
  3.文件的读取逐行打印
  4.python中序列是指，包含可变序列 列表，不可变序列字符串和元祖
  5.range的用法 range(start, stop, step)或者range(stop)。不包括stop

"""
