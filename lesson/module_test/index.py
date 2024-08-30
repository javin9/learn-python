import c7

import Animal.Cat

from Animal.Cat import sayHello

print('index.py', c7.url)  # index.py c7
c7.get_url('https://www.baidu.com')  # https://www.baidu.com
Animal.Cat.sayHello()  # Hello, world! Cat

# 绝对导入
# import Animal.Cat
# 顶级包 Animal，如果从顶级包开始导入 Animal.Cat,可以定义为

# 相对导入
# . 表示当前目录
# .. 表示上一级目录
# ... 表示上上一级目录
# 不能在入口文件里 使用相对导入，只能绝对导入
# import .Animal.Cat 会报语法错误  不能在入口文件里 通过import 使用相对导入
# from .Animal.Cat import sayHello 也会报错

sayHello()
