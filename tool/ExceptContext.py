import traceback


class ExceptContext():

    def __init__(self,
                 exception=Exception,
                 func_name=None,
                 errback=lambda func_name, *args: traceback.print_exception(
                     *args) is None,
                 finalback=lambda got_err: got_err):
        self.errback = errback
        self.finalback = finalback
        self.exception = exception
        self.got_err = False
        self.func_name = func_name  # or _find_caller_name(is_func=True)
        """
    :param exception: 指定要监控的异常
    :param func_name: 可以选择提供当前所在函数的名称，回调函数会提交到函数，用于跟踪
    :param errback: 提供一个回调函数，如果发生了指定异常，就调用该函数，该函数的返回值为True时不会继续抛出异常
    :param finalback: finally要做的操作
    """

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return_code = False
        if isinstance(exc_val, self.exception):
            return_code = self.errback(self.func_name, exc_type, exc_val,
                                       exc_tb)
            self.got_err = True
        self.finalback(self.got_err)
        return return_code


if __name__ == "main":
    print("test")
    got_error = False
    try:
        1 / 0
    except ZeroDivisionError:
        got_error = True
        traceback.print_exc()
    finally:
        print(got_error)
