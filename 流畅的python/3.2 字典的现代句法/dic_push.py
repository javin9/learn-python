#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
字典推导式示例
"""

# 定义电话区号数据
dial_codes = [  # ❶
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (91, 'India'),
    (62, 'Indonesia'),
    (81, 'Japan'),
    (234, 'Nigeria'),
    (92, 'Pakistan'),
    (7, 'Russia'),
    (1, 'United States'),
]

# 使用字典推导式创建国家到区号的映射
country_dial = {country: code for code, country in dial_codes}  # ❷
print("国家到区号的映射:")
print(country_dial)
# 输出: {'Bangladesh': 880, 'Brazil': 55, 'China': 86, 'India': 91, 'Indonesia': 62,
#        'Japan': 81, 'Nigeria': 234, 'Pakistan': 92, 'Russia': 7, 'United States': 1}

# 使用字典推导式和条件过滤
filtered_codes = {
    code: country.upper()  # ❣
    for country, code in sorted(country_dial.items()) if code < 70
}
print("\n区号小于70的国家（大写）:")
print(filtered_codes)
# 输出: {55: 'BRAZIL', 62: 'INDONESIA', 7: 'RUSSIA', 1: 'UNITED STATES'}
