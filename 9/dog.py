# @Time : 2020/4/30 14:14 
# @Author : Yao
# @File : dog.py 
# @Software: PyCharm

#首字母名称大写是类
class Dog():
	"""一次模拟小狗的简单尝试"""
	def __init__(self,name,age):
		"""初始化属性name和age"""
		self.name = name
		self.age = age

	def sit(self):
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		print(self.name.title() + " rolled over!")

my_dog = Dog('Jay',6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog's age is " + str(my_dog.age) + ".")

my_dog.sit()
my_dog.roll_over()




