import heapq
from collections import defaultdict

portfolio = [{
    'name': 'IBM',
    'shares': 100,
    'price': 91.1
}, {
    'name': 'AAPL',
    'shares': 50,
    'price': 543.22
}, {
    'name': 'FB',
    'shares': 200,
    'price': 21.09
}, {
    'name': 'HPQ',
    'shares': 35,
    'price': 31.75
}, {
    'name': 'YHOO',
    'shares': 45,
    'price': 16.35
}, {
    'name': 'ACME',
    'shares': 75,
    'price': 115.65
}]

expensive = heapq.nlargest(2, portfolio, key=lambda item: item["price"])
cheap = heapq.nsmallest(2, portfolio, key=lambda item: item["price"])

print("expensive", expensive, end='\n')
print("cheap", cheap, end='\n')

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
min_value = min(nums)
max_value = max(nums)
print(min_value, max_value)

dic_test = {}
dic_test.setdefault('a', []).append(1)
dic_test.setdefault('a', []).append(2)
dic_test.setdefault('a', []).append(3)
print(dic_test)

dic_test2 = defaultdict(list)
dic_test2['a'].append(1)
dic_test2['a'].append(2)
print(dic_test2)
"""_summary_
1.defaultdict(list) 用于创建一个字典，其中的值是一个列表.
2.免去了判断key是否存在的过程
"""
