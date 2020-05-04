# @Time : 2020/4/27 14:27 
# @Author : Yao
# @File : cars.py 
# @Software: PyCharm

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

# 检查特定值是否包含在列表中
print('bmw' in cars)
print('bmw' not in cars)

available_toppings = ['mushroom', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushroom', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + '.')
	else:
		print("Sorry, we don't have " + requested_topping + ".")
