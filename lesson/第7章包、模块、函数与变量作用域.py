# import 只能导入模块名
# from import 可以导入模块中的函数、类、变量等
# from module import * 会导入模块中所有的函数、类、变量等
# from module import (name1, name2) 换行用 () 括起来
# __all__ = [name1, name2] 限制 from module import * 可以导入的内容
# 包不会被重复导入

# colors = {"Green", "Black", "Blue"}
# colors.add("Red")
# colors.add("Blue")

# print(colors)
import sys
# dir 查看当前模块的所有属性
print(dir())
print(__name__, __doc__)

print(dir(sys))

# 绝对路径，是从顶级包开始找的
