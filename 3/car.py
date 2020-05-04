# @Time : 2020/4/27 7:26 
# @Author : Yao
# @File : car.py 
# @Software: PyCharm

cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort()  # 按首字母顺序，永久改变list顺序
print(cars)

cars.sort(reverse=True)  # 按首字母顺序倒序
print(cars.sort(reverse=True))  # 该方法不会返回列表
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']

print(sorted(cars))  # 临时改变顺序并返回列表，非永久
print(cars)
print(len(cars))  # 获取list长度
