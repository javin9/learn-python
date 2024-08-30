# 类

# 类变量，实例变量
# 类变量是共享的，实例变量是各自拥有的


class Student():
    # 类变量
    sum = 0

    # 构造函数
    def __init__(self, name):
        # 实例变量
        self.name = name
        # self.sum += 1
        # self.__class__.sum += 1

    def showNumber(self):
        print("学生总数为：", self.__class__.sum)


s1 = Student("石敢当")
s2 = Student("巨无霸")
s3 = Student("巨无霸")

print("sum:", s1.sum)

# 操作类变量，还是用 类方法


class NewStudent():
    # 类变量
    sum = 0

    # 构造函数
    def __init__(self, name):
        # 实例变量
        self.name = name
        # self.__class__.sum += 1

    def showNumber(self):
        print("学生总数为：", self.__class__.sum)

    @classmethod
    def add(cls):
        cls.sum += 1


NewStudent("石敢当").add()
NewStudent("巨无霸").add()

# 类 的定义
# 对象 的创建
# 构造函数可以调用
# 修改实例变量，用实例方法修改，不要直接赋值
# __methodname 为私有方法
# __methodname__ 为特殊方法 公有


class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        print("name:", self.name, "age:", self.age)


class Emplyee(Person):

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def showInfo(self):
        print("name:", self.name, "age:", self.age, "salary:", self.salary)


Emplyee("石敢当", 18, 10000).showInfo()
