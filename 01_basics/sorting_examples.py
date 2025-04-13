#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python排序示例
演示Python中不同的排序方法和算法
"""

def main():
    """主函数，演示各种排序方法"""
    print("Python排序示例")
    print("=" * 50)
    
    # 1. 使用内置的排序函数
    print("\n1. Python内置排序方法")
    print("-" * 30)
    
    # 示例列表
    numbers = [64, 25, 12, 22, 11, 1, 77, 36, 98, 45]
    strings = ["香蕉", "苹果", "橙子", "葡萄", "西瓜"]
    
    print(f"原始数字列表: {numbers}")
    
    # 使用sorted()函数 - 不改变原列表，返回新的排序列表
    sorted_numbers = sorted(numbers)
    print(f"使用sorted()升序排序: {sorted_numbers}")
    
    # 降序排序
    desc_numbers = sorted(numbers, reverse=True)
    print(f"使用sorted()降序排序: {desc_numbers}")
    
    # 使用sort()方法 - 直接修改原列表
    numbers.sort()
    print(f"使用sort()方法排序后的原列表: {numbers}")
    
    # 字符串排序
    print(f"\n原始字符串列表: {strings}")
    sorted_strings = sorted(strings)
    print(f"字符串排序: {sorted_strings}")
    
    # 2. 自定义排序
    print("\n2. 自定义排序")
    print("-" * 30)
    
    # 创建一个学生信息列表（字典列表）
    students = [
        {"name": "张三", "age": 20, "score": 85},
        {"name": "李四", "age": 22, "score": 92},
        {"name": "王五", "age": 18, "score": 78},
        {"name": "赵六", "age": 21, "score": 88}
    ]
    
    print("原始学生列表:")
    print_students(students)
    
    # 按照年龄排序
    age_sorted = sorted(students, key=lambda x: x["age"])
    print("\n按年龄排序:")
    print_students(age_sorted)
    
    # 按照分数排序（降序）
    score_sorted = sorted(students, key=lambda x: x["score"], reverse=True)
    print("\n按分数降序排序:")
    print_students(score_sorted)
    
    # 3. 实现排序算法
    print("\n3. 排序算法实现")
    print("-" * 30)
    
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print(f"测试数组: {test_array}")
    
    # 冒泡排序
    bubble_sorted = bubble_sort(test_array.copy())
    print(f"冒泡排序结果: {bubble_sorted}")
    
    # 选择排序
    selection_sorted = selection_sort(test_array.copy())
    print(f"选择排序结果: {selection_sorted}")
    
    # 插入排序
    insertion_sorted = insertion_sort(test_array.copy())
    print(f"插入排序结果: {insertion_sorted}")
    
def print_students(students):
    """打印学生信息的辅助函数"""
    for student in students:
        print(f"姓名: {student['name']}, 年龄: {student['age']}, 分数: {student['score']}")

def bubble_sort(arr):
    """冒泡排序实现"""
    n = len(arr)
    
    # 遍历所有数组元素
    for i in range(n):
        # 最后i个元素已经排好序
        for j in range(0, n-i-1):
            # 遍历数组从0到n-i-1
            # 如果当前元素大于下一个元素，交换它们
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

def selection_sort(arr):
    """选择排序实现"""
    n = len(arr)
    
    # 遍历所有数组元素
    for i in range(n):
        # 找到剩余未排序部分的最小元素的索引
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # 将找到的最小元素放到已排序序列的末尾
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

def insertion_sort(arr):
    """插入排序实现"""
    # 从第二个元素开始，假设第一个元素已经排序
    for i in range(1, len(arr)):
        key = arr[i]
        
        # 将key与之前已排序的元素比较
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # 元素向后移动
            j -= 1
        arr[j + 1] = key  # 找到正确位置，插入key
    
    return arr

if __name__ == "__main__":
    main()