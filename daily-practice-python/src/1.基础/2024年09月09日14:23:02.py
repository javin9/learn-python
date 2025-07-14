import os

# base_path = os.getcwd()
file_path = os.path.join(os.path.dirname(__file__), "data.txt")
# print(file_path)
with open(file_path) as f:
    data = f.readlines()
    for line in data:
        print(line.strip())

# 手动迭代
with open(file_path) as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='\n')


class Node():

    def __init__(self, value):
        self._value = value
        self._children = []

    def add_child(self, node):
        self._children.append(node)

    # !r 格式化字符串
    def __repr__(self):
        return 'Node———Node ({!r})'.format(self._value)

    def __iter__(self):
        return iter(self._children)


root = Node(0)
c1 = Node(1)
c2 = Node(2)
c3 = Node('example')
root.add_child(c1)
root.add_child(c2)
root.add_child(c3)

print(root)

for ch in root:
    print(ch)
