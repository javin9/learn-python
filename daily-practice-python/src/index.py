def create2():
    sum = 0
    arr = []
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if (i != k) and (i != j) and (j != k):
                    arr.append((i, j, k))
                    sum += 1
    print(arr, sum)


def fibs(max):
    count = 0
    a, b = 0, 1
    while count < max:
        yield b
        a, b = b, a + b
        count += 1


if __name__ == "__main__":
    # create2()
    ff = fibs(10)
    for i in ff:
        print(i, end=" ")
