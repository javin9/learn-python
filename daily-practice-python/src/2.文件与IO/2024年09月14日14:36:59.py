# file_path=
import os
import sys

file_path = os.path.join(os.path.dirname(__file__), "../data.txt")
print(sys.getdefaultencoding())
" dd ".strip()
" dd ".lstrip()
" dd ".rstrip()

with open(file_path, "rt") as f:
    for line in f:
        print(line.strip())

# 打印输出至文件中

file_path = os.path.join(os.path.dirname(__file__), "../a.txt")
with open(file_path, "a") as f:
    f.write("hello world\n")
