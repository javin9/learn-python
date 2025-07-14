import re

str = 'SDD76DS9877wer88654sdfer'

result = re.match(r'\d+', str)  # 匹配数字
print(result)

result = re.search(r'\d+', str)  # 匹配字母
print(result.group())

new_str = re.sub(r'\d+', '____', str)
print(new_str)
