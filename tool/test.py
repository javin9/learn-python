# coding: utf-8
class C:

    def __init__(self):
        print("init")

    def __enter__(self):
        print("enter")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

    def __del__(self):
        print("del")


if __name__ == '__main__':
    a = C()
    print("st")
    with a:
        print("hi")
    with a:
        print("heelo")
    print("ed")
