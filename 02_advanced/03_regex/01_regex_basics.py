#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python正则表达式基础
"""

# 正则表达式是一种用于匹配字符串模式的特殊序列
# Python通过re模块提供对正则表达式的支持

import re

print("===== 正则表达式基础 =====")

# 1. 基本匹配
print("\n1. 基本匹配")
pattern = "python"
text = "I love python programming"
result = re.search(pattern, text)
print(f"匹配'{pattern}'在'{text}'中: {'找到' if result else '未找到'}")
if result:
    print(f"匹配位置: {result.start()}-{result.end()}, 匹配内容: {result.group()}")

# 2. 元字符
print("\n2. 元字符")
# . (点) - 匹配任意字符(除了换行符)
pattern = "py...n"
text = "python"
result = re.search(pattern, text)
print(f"使用'.': '{pattern}'匹配'{text}': {'成功' if result else '失败'}")

# ^ (脱字符) - 匹配字符串开头
pattern = "^Python"
texts = ["Python is fun", "I love Python"]
for text in texts:
    result = re.search(pattern, text)
    print(f"使用'^': '{pattern}'匹配'{text}': {'成功' if result else '失败'}")

# $ (美元符) - 匹配字符串结尾
pattern = "Python$"
texts = ["I love Python", "Python is fun"]
for text in texts:
    result = re.search(pattern, text)
    print(f"使用'$': '{pattern}'匹配'{text}': {'成功' if result else '失败'}")

# 3. 字符类
print("\n3. 字符类")
# [] - 表示一组字符，匹配其中任意一个
pattern = "[Pp]ython"  # 匹配Python或python
texts = ["Python", "python"]
for text in texts:
    result = re.search(pattern, text)
    print(f"使用'[]': '{pattern}'匹配'{text}': {'成功' if result else '失败'}")

# [^] - 否定字符集，匹配不在集合中的任意字符
pattern = "[^0-9]"  # 匹配非数字
text = "Python3"
result = re.search(pattern, text)
print(f"使用'[^]': '{pattern}'匹配'{text}中第一个非数字': {result.group() if result else '失败'}")

# 4. 重复
print("\n4. 重复")
# * - 匹配前一个字符0次或多次
pattern = "py.*n"
texts = ["pyn", "python", "pythoooooon"]
for text in texts:
    result = re.search(pattern, text)
    print(f"使用'*': '{pattern}'匹配'{text}': {'成功' if result else '失败'}")

# + - 匹配前一个字符1次或多次
pattern = "py.+n"
texts = ["pyn", "python", "pn"]
for text in texts:
    result = re.search(pattern, text)
    print(f"使用'+': '{pattern}'匹配'{text}': {'成功' if result else '失败'}")

# ? - 匹配前一个字符0次或1次
pattern = "colou?r"  # 匹配color或colour
texts = ["color", "colour"]
for text in texts:
    result = re.search(pattern, text)
    print(f"使用'?': '{pattern}'匹配'{text}': {'成功' if result else '失败'}")

# {n} - 精确匹配n次
# {n,} - 匹配至少n次
# {n,m} - 匹配n到m次
pattern = "a{2,3}"  # 匹配2到3个连续的a
texts = ["a", "aa", "aaa", "aaaa"]
for text in texts:
    result = re.search(pattern, text)
    print(f"使用'{{2,3}}': '{pattern}'匹配'{text}': {'成功' if result else '失败'}")

# 5. 转义字符
print("\n5. 转义字符")
# 使用\可以转义特殊字符
pattern = r"\."  # 匹配点号，不是任意字符
text = "www.example.com"
result = re.search(pattern, text)
print(f"使用'\\': '{pattern}'匹配'{text}'中的点号: {'成功' if result else '失败'}")
if result:
    print(f"匹配位置: {result.start()}")

print("\n正则表达式基础语法学习完成！在下一节中，我们将学习Python的re模块更多功能。") 