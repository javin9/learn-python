def debugger(func):

    def wrapper(*args, **kwargs):
        print(f"Function name: {func.__name__}")
        func(*args, **kwargs)
        print(f"Arguments: {args}")

    return wrapper


if __name__ == "__main__":
    vary = {"a": 2}

    @debugger
    def fun():
        print("Hello")

    fun()
