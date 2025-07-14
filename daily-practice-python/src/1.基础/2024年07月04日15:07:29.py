# daily-practice-python/src/2024年07月04日11:05:33.py
# 1.12 序列中出现次数最多的元素
#

from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't",
    'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're",
    'under'
]

top_three = Counter(words).most_common(3)
print(top_three)

print("-----------------")
a = Counter(words)
print(a)
"""_summary_
1.Counter 是一个简单的计数器，用来统计字符出现的个数
"""
