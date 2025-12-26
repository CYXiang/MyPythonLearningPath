#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python re模块详解
"""

import re

print("===== Python re模块功能 =====")

# 1. 常用函数
print("\n1. 常用函数")

text = "Python is amazing. Python is powerful."

# re.search() - 查找第一个匹配
result = re.search(r"Python", text)
print(f"re.search(): {result.group() if result else '未找到'}")

# re.match() - 只在字符串开头匹配
result = re.match(r"Python", text)
print(f"re.match(): {result.group() if result else '未找到'}")

# 测试re.match()不匹配的情况
result = re.match(r"amazing", text)
print(f"re.match('amazing'): {result.group() if result else '未找到'}")

# re.findall() - 查找所有匹配，返回列表
result = re.findall(r"Python", text)
print(f"re.findall(): {result}")

# re.finditer() - 查找所有匹配，返回迭代器
result = re.finditer(r"Python", text)
print("re.finditer():")
for match in result:
    print(f"  位置: {match.start()}-{match.end()}, 匹配: {match.group()}")

# re.split() - 分割字符串
result = re.split(r"\.", text)
print(f"re.split(): {result}")

# re.sub() - 替换匹配的文本
result = re.sub(r"Python", "Ruby", text)
print(f"re.sub(): {result}")

# 2. 编译正则表达式
print("\n2. 编译正则表达式")
# 当多次使用同一正则表达式时，使用compile()可提高效率
regex = re.compile(r"Python")
result = regex.findall(text)
print(f"编译后findall(): {result}")
result = regex.sub("Java", text)
print(f"编译后sub(): {result}")

# 3. 分组
print("\n3. 分组")
# 使用()进行分组捕获
text = "My email is user@example.com"
pattern = r"(\w+)@(\w+)\.(\w+)"
result = re.search(pattern, text)
if result:
    print(f"完整匹配: {result.group(0)}")
    print(f"第1组(用户名): {result.group(1)}")
    print(f"第2组(域名): {result.group(2)}")
    print(f"第3组(顶级域名): {result.group(3)}")
    
    # 使用groups()获取所有分组
    print(f"所有分组: {result.groups()}")

# 命名分组
pattern = r"(?P<username>\w+)@(?P<domain>\w+)\.(?P<tld>\w+)"
result = re.search(pattern, text)
if result:
    print(f"命名分组 - 用户名: {result.group('username')}")
    print(f"命名分组 - 域名: {result.group('domain')}")
    print(f"命名分组 - 顶级域名: {result.group('tld')}")
    
    # 使用groupdict()获取所有命名分组
    print(f"所有命名分组: {result.groupdict()}")

# 4. 标志(flags)
print("\n4. 标志(flags)")

# re.IGNORECASE (re.I) - 忽略大小写
text = "Python is different from python"
pattern = r"python"
result = re.findall(pattern, text)
print(f"不使用忽略大小写: {result}")

result = re.findall(pattern, text, re.IGNORECASE)
print(f"使用忽略大小写(re.I): {result}")

# re.MULTILINE (re.M) - 多行模式
text = """Line 1
Line 2
Line 3"""
pattern = r"^Line"  # 匹配以'Line'开头的行
result = re.findall(pattern, text)
print(f"不使用多行模式: {result}")

result = re.findall(pattern, text, re.MULTILINE)
print(f"使用多行模式(re.M): {result}")

# re.DOTALL (re.S) - 让.匹配包括换行符在内的所有字符
text = """Line 1
Line 2"""
pattern = r"Line 1.+Line 2"
result = re.search(pattern, text)
print(f"不使用DOTALL: {'匹配' if result else '未匹配'}")

result = re.search(pattern, text, re.DOTALL)
print(f"使用DOTALL(re.S): {'匹配' if result else '未匹配'}")

# 5. 贪婪与非贪婪匹配
print("\n5. 贪婪与非贪婪匹配")

# 贪婪模式 - 尽可能多地匹配字符
text = "<h1>标题</h1><p>段落</p>"
pattern = r"<.+>"
result = re.search(pattern, text)
print(f"贪婪匹配: {result.group() if result else '未匹配'}")

# 非贪婪模式 - 尽可能少地匹配字符
pattern = r"<.+?>"
result = re.search(pattern, text)
print(f"非贪婪匹配: {result.group() if result else '未匹配'}")

# 查找所有非贪婪匹配
result = re.findall(pattern, text)
print(f"所有非贪婪匹配: {result}")

print("\nPython re模块学习完成！在下一节中，我们将学习常用的正则表达式模式。") 