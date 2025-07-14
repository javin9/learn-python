import re

text = 'yeah, but no, but yeah, but no, but yeah'

index = text.find("no22")  # 10
print(index)
print(text.startswith('yeah'))  # 单个 True
print(text.startswith(('yeah', "but")))  # 多个 True

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

# text = '11/27/2012'
result = re.match(r'\d+/\d+/\d+', text)  # 匹配成功
print(result)

datepat = re.compile(r'\d+/\d+/\d+')
result = datepat.findall(text)  # ['11/27/2012', '3/13/2013']
print("result", result)
"""
find, startswith, endswith 可以查询多个字符串，只要其中一个匹配即可。
当写正则式字符串的时候，相对普遍的做法是使用原始字符串比如 r'(\d+)/(\d+)/(\d+)' 。 这种字符串将不去解析反斜杠，这在正则表达式中是很有用的。 如果不这样做的话，你必须使用两个反斜杠，类似 '(\\d+)/(\\d+)/(\\d+)'
"""
result = re.findall(r'(\d+)/(\d+)/(\d+)', text)
print("result", result)  # [('1', '1', '2'), ('3', '1', '3')]
