# 2024年07月05日10:23:12
from operator import attrgetter


class User:

    def __init__(self, id, name, email):
        self.name = name
        self.id = id

    def __repr__(self):
        return f"User({self.id!r}, {self.name!r})"


User(1, "user1")

sorted([User(1, "user1"), User(2, "user2"),
        User(3, "user3")],
       key=lambda x: x.id)

sorted([User(1, "user1"), User(2, "user2"),
        User(3, "user3")],
       key=attrgetter("id", "name"))

min([User(1, "user1"), User(2, "user2")], key=attrgetter("id"))
max([User(1, "user1"), User(2, "user2")], key=lambda x: x.id)

#
"""_summary_
0.operator的itemgetter()，attrgetter（）
1. attrgetter() 函数用于从对象中获取指定元素
2. sorted排序
 """
