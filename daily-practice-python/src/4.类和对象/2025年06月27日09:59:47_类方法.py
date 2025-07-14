# 静态方法
# 使用场景 将相关功能集中到类的命名空间中，避免全局函数的散乱


class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b


print(MathUtils.add(5, 3))  # 输出: 8
print(MathUtils.add(5, 3))  # 输出: 8


# 类方法
class MyClass:
    class_variable = "I am a class variable"

    @classmethod
    def class_method(cls):
        return f"Class method called, accessing {cls.class_variable}"

    @classmethod
    def create_instance(cls, value):
        # 工厂方法：创建并返回实例
        return cls(value)

    def __init__(self, value):
        self.value = value


# 通过类调用
print(MyClass.class_method()
      )  # 输出: Class method called, accessing I am a class variable

# 通过类方法创建实例
instance = MyClass.create_instance("test")
print(instance.value)  # 输出: test

# 通过实例调用类方法
print(instance.class_method()
      )  # 输出: Class method called, accessing I am a class variable

###
# staticmethod 静态方法 只是为了聚合到一起
# classmethod
