import re

text = "The year is 2025."

# 使用 re.search()
# re.search()：在整个字符串中搜索，找到第一个匹配的子串并返回匹配对象。如果没有找到，则返回 None。

search_result = re.search(r'\d{4}', text)
if search_result:
    print("search:", search_result.group())  # 输出: search: 2025

# 使用 re.match()
# re.match()：只从字符串的开头开始匹配。如果字符串开头不符合正则表达式，即使后面有匹配的子串，也会返回 None。

match_result = re.match(r'\d{4}', text)
if match_result:
    print("match___1:", match_result.group())  # 无输出，因为字符串开头不是数字

# 如果字符串以数字开头
text2 = "2025 is the year."
match_result = re.match(r'\d{4}', text2)
if match_result:
    print("match___2:", match_result.group())  # 输出: match: 2025

text = "Years: 2023, 2024, 2025"
matches = re.findall(r'\d{4}', text)
print(matches)  # 输出: ['2023', '2024', '2025']

text = "Years: 2023, 2024, 2025"
for match in re.finditer(r'\d{4}', text):
    print(f"Found {match.group()} at {match.start()}-{match.end()}")
# 输出:
# Found 2023 at 7-11
# Found 2024 at 13-17
# Found 2025 at 19-23

text = "Year 2023 and 2024"
result = re.sub(r'\d{4}', 'XXXX', text)
print(result)  # 输出: Year XXXX and XXXX
# 使用函数替换 substitute
result = re.sub(r'\d{4}', lambda m: str(int(m.group()) + 1), text)
print(result)  # 输出: Year 2024 and 2025
