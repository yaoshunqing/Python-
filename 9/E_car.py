# @Time : 2020/4/30 17:46 
# @Author : Yao
# @File : E_car.py 
# @Software: PyCharm

from Car import Car

class Battery():
	def __init__(self,battery_size = 70):
		self.battery_size = battery_size

	def describe_battery(self):
		print("This car has a " + str(self.battery_size) + "-kWh battery.")


class ElectricCar(Car):
	#继承类
	def __init__(self, make, model, year, battery):
		#初始化父类属性
		super().__init__(make, model, year)
		self.battery = Battery(battery)

	# def describe_battery(self):
	# 	print("This car has a " + str(self.battery_size) + "-kWh battery.")

	def fill_gas_tank(self):
		#重写父类方法会自动覆盖父类方法
		print("This car has no gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016, 50)
print(my_tesla.get_descriptive_name())


my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
