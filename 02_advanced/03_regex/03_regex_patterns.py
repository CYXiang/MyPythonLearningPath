#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
常用正则表达式模式
"""

import re

print("===== 常用正则表达式模式 =====")

def test_pattern(pattern, test_strings, pattern_name=""):
    """测试正则表达式模式"""
    print(f"\n{pattern_name}模式 ({pattern}):")
    for test_string in test_strings:
        match = re.fullmatch(pattern, test_string)
        print(f"  '{test_string}': {'匹配' if match else '不匹配'}")

# 1. 数字匹配
print("\n1. 数字匹配")

# 整数
pattern = r"^-?\d+$"
test_strings = ["123", "-456", "0", "abc", "123a"]
test_pattern(pattern, test_strings, "整数")

# 小数
pattern = r"^-?\d+(\.\d+)?$"
test_strings = ["123", "123.45", "-456.78", "0.5", "abc", "123."]
test_pattern(pattern, test_strings, "小数")

# 科学计数法
pattern = r"^-?\d+(\.\d+)?([eE][+-]?\d+)?$"
test_strings = ["123", "1.23e5", "1.23E-4", "-1.23e+5", "abc"]
test_pattern(pattern, test_strings, "科学计数法")

# 2. 字符串匹配
print("\n2. 字符串匹配")

# 仅包含字母
pattern = r"^[a-zA-Z]+$"
test_strings = ["abc", "XYZ", "AbCdEf", "123", "abc123"]
test_pattern(pattern, test_strings, "仅字母")

# 仅包含字母和数字
pattern = r"^[a-zA-Z0-9]+$"
test_strings = ["abc", "123", "abc123", "abc_123"]
test_pattern(pattern, test_strings, "字母和数字")

# 仅包含中文汉字
pattern = r"^[\u4e00-\u9fa5]+$"
test_strings = ["你好", "中文", "Python", "Python中文"]
test_pattern(pattern, test_strings, "仅中文汉字")

# 3. 常见格式验证
print("\n3. 常见格式验证")

# 邮箱地址
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
test_strings = ["user@example.com", "user.name@example.co.uk", "user@example", "user@.com", "@example.com"]
test_pattern(pattern, test_strings, "邮箱地址")

# URL
pattern = r"^(https?|ftp)://[^\s/$.?#].[^\s]*$"
test_strings = ["http://example.com", "https://example.com/path", "ftp://example.com", "example.com", "http://"]
test_pattern(pattern, test_strings, "URL")

# 中国手机号码
pattern = r"^1[3-9]\d{9}$"
test_strings = ["13812345678", "15912345678", "19912345678", "12345678901", "1381234567"]
test_pattern(pattern, test_strings, "中国手机号码")

# 中国身份证号(18位)
pattern = r"^\d{17}[\dXx]$"
test_strings = ["110101199001011234", "11010119900101123X", "1101011990010112345", "11010119900101123"]
test_pattern(pattern, test_strings, "中国身份证号")

# IP地址(IPv4)
pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
test_strings = ["192.168.1.1", "255.255.255.255", "0.0.0.0", "256.0.0.1", "192.168.1"]
test_pattern(pattern, test_strings, "IPv4地址")

# 日期 (YYYY-MM-DD)
pattern = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
test_strings = ["2023-01-01", "2023-12-31", "2023-02-30", "2023-13-01", "01-01-2023"]
test_pattern(pattern, test_strings, "日期")

# 4. 特殊匹配
print("\n4. 特殊匹配")

# 密码强度(至少包含大小写字母、数字和特殊字符，长度8-20)
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,20}$"
test_strings = ["Passw0rd!", "password", "PASSWORD", "pass", "P@ssw0rd1234567890123"]
test_pattern(pattern, test_strings, "强密码")

# 匹配HTML标签
pattern = r"<([a-z]+)([^<]+)*(?:>(.*)<\/\1>|\s+\/>)"
test_strings = ["<div>内容</div>", "<img src='image.jpg'/>", "<div>内容", "div>内容</div>"]
test_pattern(pattern, test_strings, "HTML标签")

print("\n常用正则表达式模式学习完成！在下一节中，我们将学习正则表达式的实际应用案例。") 