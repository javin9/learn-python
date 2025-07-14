from enum import Enum
from enum import IntEnum, unique


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


# 枚举就是一个类
print(Color.RED)
print(Color.RED.name)
print(Color.RED.value)
print(Color.RED.value == 1)
print(Color.RED == Color.RED)

# key不重复
# value不可以重复
# 枚举类型不可变
# 枚举类型可以遍历
print("--------------")
for color in Color:
    print(color, color.name, color.value)

# 转换枚举类型
print("-----转换枚举类型---------")
print(Color(1))

#
print("-----IntEnum---------")


@unique
class VIP(IntEnum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4
