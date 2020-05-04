# @Time : 2020/4/29 19:58 
# @Author : Yao
# @File : pizza.py 
# @Software: PyCharm

def make_pizza(size,*toppings):
	"""打印顾客点的配料"""
	print("\nMaking a " + str(size) + " pizza with the following toppings: ")
	for topping in toppings:
		print("- " + topping)

# make_pizza(12,'pepperoni')
# make_pizza(16,'pepperoni','mushroom','extra cheese')

def build_profile(first,last,**user_info):
	"""创建字典，，记录用户所有信息"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for k,v in user_info.items():
		profile[k] = v
	return profile

#user_info = {'location':'china','phone':'15600931079'}

# b = build_profile('sq','Y',location='china',phone='15600931079')
# print(b)




