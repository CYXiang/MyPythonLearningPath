#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
这是我的第一个Python程序
用于测试Python环境是否正常安装
"""

def main():
    """主函数，打印欢迎信息"""
    print("你好，Python！")
    print("开始我的Python学习之旅！")
    
    # 展示一些基础语法
    name = "学习者"
    age = 25
    is_programmer = True
    
    print(f"我是{name}，今年{age}岁。")
    
    if is_programmer:
        print("我已经是一名程序员了！")
    else:
        print("我正在成为一名程序员！")
    
    # 简单循环示例
    print("\n数到10：")
    for i in range(1, 11):
        print(i, end=" ")
    
    print("\n\n准备好开始学习了！")

if __name__ == "__main__":
    main() 