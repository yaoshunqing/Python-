# @Time : 2020/4/27 9:16
# @Author : Yao
# @File : numbers-列表基本处理.py
# @Software: PyCharm

numbers = list(range(1, 6))
print(numbers)

squares = []
for value in range(1, 11):
	squares.append(value ** 2)
print(squares)

# 数字列表简单统计
digits = [1, 3, 5, 2, 9, 6, 6, 0]

print(max(digits))  # 最大值
print(min(digits))  # 最小值
print(sum(digits))  # 求和

digits.sort()
print(digits)  # 从小到大排序，永久改变
digits.sort(reverse=True)
print(digits)  # 从大到小排序，永久改变

# 列表解析
squares = [i ** 2 for i in range(1, 11)]  # 比起上面的方法更省事儿
print(squares)

# 切片
numbers = [1, 2, 3, 4, 5]
print(numbers[1:3])
print(numbers[:3])  # 默认从最初开始
print(numbers[2:4])
print(numbers[-3:])  # 从倒数第三开始

# 复制列表
Newnumbers = numbers[:]  # 复制列表
numbers.append(6)
print(Newnumbers)
Newnumbers = numbers  # 两个列表将相互关联，任何的改变两者都会有变化
numbers.append(7)
print(Newnumbers)
