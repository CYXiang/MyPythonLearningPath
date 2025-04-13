# Python基本数据类型与变量示例

# --------------------------------------
# 1. 数字类型 (Numeric Types)
# --------------------------------------

# 整数 (int)
my_int = 10
print(f"整数示例: {my_int}, 类型: {type(my_int)}")

# 浮点数 (float)
my_float = 3.14
print(f"浮点数示例: {my_float}, 类型: {type(my_float)}")

# 复数 (complex)
my_complex = 1 + 2j
print(f"复数示例: {my_complex}, 类型: {type(my_complex)}")

# 进制表示
binary_num = 0b1010  # 二进制
print(f"二进制1010 = {binary_num}")

hex_num = 0xFF      # 十六进制
print(f"十六进制FF = {hex_num}")

# --------------------------------------
# 2. 字符串 (str)
# --------------------------------------
my_string = "Hello, Python!"
print(f"字符串示例: {my_string}, 类型: {type(my_string)}")

# 字符串切片
print(f"前5个字符: {my_string[:5]}")
print(f"最后7个字符: {my_string[-7:]}")

# 字符串方法
print(f"大写: {my_string.upper()}")
print(f"替换: {my_string.replace('Python', 'World')}")

# f-strings (Python 3.6+)
name = "Python"
print(f"我正在学习 {name}!")

# --------------------------------------
# 3. 布尔类型 (bool)
# --------------------------------------
my_true = True
my_false = False
print(f"布尔值示例: {my_true}, {my_false}")
print(f"布尔运算: {my_true and my_false}, {my_true or my_false}")

# --------------------------------------
# 4. 列表 (list)
# --------------------------------------
my_list = [1, 2, 3, "Python", True]
print(f"列表示例: {my_list}, 类型: {type(my_list)}")

# 列表操作
my_list.append("新元素")
print(f"添加元素后: {my_list}")
print(f"列表第3个元素: {my_list[2]}")
print(f"列表切片: {my_list[1:4]}")

# --------------------------------------
# 5. 元组 (tuple)
# --------------------------------------
my_tuple = (1, 2, "Python", True)
print(f"元组示例: {my_tuple}, 类型: {type(my_tuple)}")
print(f"元组第2个元素: {my_tuple[1]}")

# 元组不可修改
# my_tuple[0] = 10  # 这会报错

# --------------------------------------
# 6. 集合 (set)
# --------------------------------------
my_set = {1, 2, 3, 3, 4, 4, 5}  # 自动去重
print(f"集合示例: {my_set}, 类型: {type(my_set)}")

# 集合操作
new_set = {3, 4, 5, 6, 7}
print(f"并集: {my_set | new_set}")
print(f"交集: {my_set & new_set}")
print(f"差集: {my_set - new_set}")

# --------------------------------------
# 7. 字典 (dict)
# --------------------------------------
my_dict = {"name": "Python", "version": 3.9, "is_fun": True}
print(f"字典示例: {my_dict}, 类型: {type(my_dict)}")

# 字典操作
print(f"获取值: {my_dict['name']}")
my_dict["new_key"] = "新值"
print(f"添加键值对后: {my_dict}")

# --------------------------------------
# 8. 变量特性
# --------------------------------------
# 动态类型
x = 10
print(f"x = {x}, 类型: {type(x)}")
x = "现在是字符串"
print(f"x = {x}, 类型: {type(x)}")

# 变量赋值
a = b = c = 1  # 多重赋值
print(f"a = {a}, b = {b}, c = {c}")

x, y, z = 1, "字符串", True  # 序列解包
print(f"x = {x}, y = {y}, z = {z}")

# --------------------------------------
# 9. None 类型
# --------------------------------------
my_none = None
print(f"None值示例: {my_none}, 类型: {type(my_none)}")
