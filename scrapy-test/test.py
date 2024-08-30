class Test:

    def __init__(self):
        pass

    def test(self):
        number_list = [1, 2, 3, 4, 5]
        for item in number_list:
            n = self.parse(item)
            for i in n:
                print(i)

    def parse(self, value):
        yield value * value


if __name__ == '__main__':
    Test().test()
    print('Hello World')
