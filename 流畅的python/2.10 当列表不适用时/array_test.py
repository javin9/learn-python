#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=== 数组类型码说明 ===
'b': 有符号字符 (-128 to 127)
'B': 无符号字符 (0 to 255)
'h': 有符号短整数 (-32768 to 32767)
'H': 无符号短整数 (0 to 65535)
'i': 有符号整数
'I': 无符号整数
'l': 有符号长整数
'L': 无符号长整数
'f': 浮点数
'd': 双精度浮点数
'u': Unicode字符

=== 使用场景对比 ===
列表适用场景:
1. 存储不同类型的数据
2. 需要频繁插入、删除操作
3. 数据结构复杂（嵌套、混合类型）
4. 一般性的数据处理

数组适用场景:
1. 大量相同类型的数据
2. 数值计算和科学计算
3. 内存使用要求严格
4. 需要与C扩展交互
5. 音频、图像等二进制数据处理
"""

import array
import sys
import time


def demo_builtin_array():
    """演示内置 array 模块的用法"""
    print("=== 内置 array 模块演示 ===")

    # 1. 创建不同类型的数组
    # 'i' 表示有符号整数
    int_array = array.array('i', [1, 2, 3, 4, 5])
    print(f"整数数组: {int_array}")

    # 'f' 表示浮点数
    float_array = array.array('f', [1.1, 2.2, 3.3, 4.4, 5.5])
    print(f"浮点数组: {float_array}")

    # 'u' 表示Unicode字符
    unicode_array = array.array('u', 'hello')
    print(f"Unicode数组: {unicode_array}")

    # 2. 数组操作
    print("\n--- 数组操作 ---")

    # 添加元素
    int_array.append(6)
    print(f"添加元素后: {int_array}")

    # 扩展数组
    int_array.extend([7, 8, 9])
    print(f"扩展后: {int_array}")

    # 插入元素
    int_array.insert(0, 0)
    print(f"插入元素后: {int_array}")

    # 删除元素
    int_array.remove(5)
    print(f"删除元素后: {int_array}")

    # 索引访问
    print(f"第一个元素: {int_array[0]}")
    print(f"最后一个元素: {int_array[-1]}")

    # 切片
    print(f"前三个元素: {int_array[:3]}")


def demo_list_vs_array():
    """演示列表与数组的区别"""
    print("\n=== 列表 vs 数组对比 ===")

    # 创建列表和数组
    python_list = [1, 2, 3, 4, 5] * 1000
    int_array = array.array('i', [1, 2, 3, 4, 5] * 1000)

    # 内存使用对比
    print(f"列表内存使用: {sys.getsizeof(python_list)} bytes")
    print(f"数组内存使用: {sys.getsizeof(int_array)} bytes")


def main():
    """主函数"""
    print("Python 数组使用指南")
    print("=" * 50)

    demo_builtin_array()
    demo_list_vs_array()


if __name__ == "__main__":
    main()
