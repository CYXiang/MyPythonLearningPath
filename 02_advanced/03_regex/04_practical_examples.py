#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
正则表达式实际应用案例
"""

import re
import os

print("===== 正则表达式实际应用案例 =====")

# 1. 从文本中提取信息
print("\n1. 从文本中提取信息")

# 提取邮箱地址
text = """联系方式：
李明: liming@example.com
张华: zhanghua@company.cn
王强的邮箱是 wangqiang123@gmail.com，请尽快联系他。
"""

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_pattern, text)
print("提取邮箱地址:")
for i, email in enumerate(emails, 1):
    print(f"  {i}. {email}")

# 提取电话号码
text = """
联系电话：
- 李明: 13812345678
- 张华: 139-1234-5678
- 服务热线: 400-123-4567
- 座机: 010-12345678
"""

phone_pattern = r'(1[3-9]\d{9}|1[3-9]\d{1}-\d{4}-\d{4}|400-\d{3}-\d{4}|\d{3,4}-\d{8})'
phones = re.findall(phone_pattern, text)
print("\n提取电话号码:")
for i, phone in enumerate(phones, 1):
    print(f"  {i}. {phone}")

# 2. 数据清洗
print("\n2. 数据清洗")

# 清洗文本中的HTML标签
html_text = "<p>这是一个<b>示例</b>文本，包含<a href='https://example.com'>链接</a>和其他HTML标签。</p>"
clean_text = re.sub(r'<[^>]+>', '', html_text)
print(f"原始HTML: {html_text}")
print(f"清洗后文本: {clean_text}")

# 日期格式化 - 将不同格式的日期统一为YYYY-MM-DD
dates = ["2023/01/15", "01-15-2023", "2023.01.15"]
print("\n日期格式化:")
for date in dates:
    # 匹配不同格式的日期并提取年月日
    match = re.search(r'(\d{4})[/.-](\d{1,2})[/.-](\d{1,2})|(\d{1,2})[/.-](\d{1,2})[/.-](\d{4})', date)
    if match:
        groups = match.groups()
        if groups[0]:  # YYYY/MM/DD格式
            year, month, day = groups[0], groups[1], groups[2]
        else:  # MM/DD/YYYY格式
            month, day, year = groups[3], groups[4], groups[5]
        # 统一格式化为YYYY-MM-DD
        formatted_date = f"{year}-{int(month):02d}-{int(day):02d}"
        print(f"  {date} -> {formatted_date}")

# 3. 文本分割和替换
print("\n3. 文本分割和替换")

# 分割CSV文本行
csv_text = "姓名,年龄,职业,薪资\n李明,28,工程师,15000\n张华,35,\"经理,总监\",25000\n王强,24,设计师,12000"
print("分割CSV文本：")

# 正确处理CSV中的引号内逗号
for line in csv_text.split('\n'):
    # 使用正则表达式处理引号内的逗号
    fields = re.findall(r'(?:"([^"]*)")|([^,]+)', line)
    # 合并结果，每个字段可能在匹配组1或组2中
    row = [f[0] if f[0] else f[1] for f in fields]
    print(f"  {row}")

# 替换敏感信息
sensitive_text = "李明的身份证号是11010119900101XXXX，手机号是138XXXXXXXX。"
# 身份证号码打码
masked_text = re.sub(r'(\d{6})\d{8}(\w{4})', r'\1********\2', sensitive_text)
# 手机号打码
masked_text = re.sub(r'(1[3-9]\d{2})\d{4}(\d{4})', r'\1****\2', masked_text)
print(f"\n敏感信息处理:")
print(f"  原文: {sensitive_text}")
print(f"  处理后: {masked_text}")

# 4. 复杂文本解析
print("\n4. 复杂文本解析")

# 解析日志文件
log_text = """
[2023-01-15 08:32:15] [INFO] 用户登录: user123
[2023-01-15 08:35:28] [ERROR] 数据库连接失败: Connection refused
[2023-01-15 09:15:44] [WARNING] 内存使用率超过80%
[2023-01-15 10:27:33] [INFO] 用户登出: user123
"""

print("日志解析:")
log_pattern = r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] \[(\w+)\] (.+)'
log_matches = re.finditer(log_pattern, log_text)
for i, match in enumerate(log_matches, 1):
    timestamp, level, message = match.groups()
    print(f"  日志{i}:")
    print(f"    时间: {timestamp}")
    print(f"    级别: {level}")
    print(f"    消息: {message}")

# 5. 验证输入
print("\n5. 验证输入")

def validate_input(input_text, input_type):
    """验证输入是否符合特定格式"""
    patterns = {
        'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        'phone': r'^1[3-9]\d{9}$',
        'username': r'^[a-zA-Z][a-zA-Z0-9_]{2,19}$',  # 以字母开头，可包含字母、数字和下划线，长度3-20
        'password': r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,20}$'  # 强密码
    }
    
    if input_type not in patterns:
        return False
    
    pattern = patterns[input_type]
    return bool(re.fullmatch(pattern, input_text))

test_inputs = {
    'email': ['user@example.com', 'invalid-email', 'user@domain'],
    'phone': ['13812345678', '123456789', '23812345678'],
    'username': ['user123', '123user', 'u', 'user_name'],
    'password': ['Passw0rd!', 'password', 'PASSWORD123', 'Aa1!']
}

print("输入验证:")
for input_type, values in test_inputs.items():
    print(f"  {input_type}验证:")
    for value in values:
        is_valid = validate_input(value, input_type)
        print(f"    '{value}': {'有效' if is_valid else '无效'}")

# 6. 实用正则表达式综合案例：简单网页爬虫
print("\n6. 实用正则表达式综合案例：简单网页爬虫模拟")

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>示例网页</title>
    <meta charset="UTF-8">
    <meta name="description" content="这是一个用于测试的示例网页">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>欢迎访问示例网站</h1>
        <nav>
            <ul>
                <li><a href="index.html">首页</a></li>
                <li><a href="about.html">关于我们</a></li>
                <li><a href="contact.html">联系方式</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <article>
            <h2>公司新闻</h2>
            <p>我们公司最近推出了新产品，详情请访问<a href="https://example.com/products">产品页面</a>。</p>
            <p>联系销售: <a href="mailto:sales@example.com">sales@example.com</a>或拨打<tel>400-123-4567</tel></p>
        </article>
        
        <aside>
            <h3>联系方式</h3>
            <p>电子邮件: <a href="mailto:info@example.com">info@example.com</a></p>
            <p>电话: 010-12345678</p>
            <p>地址: 北京市海淀区XX路XX号</p>
        </aside>
    </main>
    
    <footer>
        <p>&copy; 2023 示例公司. 保留所有权利.</p>
    </footer>
</body>
</html>
"""

print("网页爬虫模拟: 提取网页信息")

# 提取网页标题
title_pattern = r'<title>(.*?)</title>'
title_match = re.search(title_pattern, html_content)
if title_match:
    print(f"  网页标题: {title_match.group(1)}")

# 提取所有链接
link_pattern = r'<a\s+[^>]*href=["\'](.*?)["\'][^>]*>(.*?)</a>'
links = re.findall(link_pattern, html_content)
print("  链接列表:")
for url, text in links:
    print(f"    - {text}: {url}")

# 提取所有标题标签内容
heading_pattern = r'<h([1-6])>(.*?)</h\1>'
headings = re.findall(heading_pattern, html_content)
print("  标题层次结构:")
for level, text in headings:
    print(f"    {'#'*int(level)} {text}")

# 提取联系信息
email_pattern = r'[\w.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_pattern, html_content)
print("  邮箱地址:")
for email in emails:
    print(f"    - {email}")

phone_pattern = r'((?:(?:\d{3,4}[-\s]?)?\d{3,4}[-\s]?\d{4})|(?:400[-\s]?\d{3}[-\s]?\d{4}))'
phones = re.findall(phone_pattern, html_content)
print("  电话号码:")
for phone in phones:
    print(f"    - {phone}")

print("\n正则表达式实际应用案例学习完成！现在您已经掌握了正则表达式的基础和应用方法。") 