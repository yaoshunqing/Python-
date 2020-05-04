# @Time : 2020/4/29 15:18 
# @Author : Yao
# @File : greeter.py 
# @Software: PyCharm

def greet_user(username):
	# 三引号既可以用来分行写字符串，也可以用来注释
	"""显示简单的问候语"""
	print("Hello, " + username.title() + "!")


greet_user("nao")


def describe_pet(animal_type, pet_name="dog"):
	"""显示宠物信息"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name + ".")


# 关键字实参
describe_pet(animal_type="hamster", pet_name="HH")
# 形式参数默认值dog
describe_pet(animal_type="hamster")



def greet_user(username):
	# 三引号既可以用来分行写字符串，也可以用来注释
	"""显示简单的问候语"""
	for name in username:
		print("Hello, " + name.title() + "!")


greet_user(['nao','yao','hah'])


#禁止函数修改列表，可以通过传递列表副本给函数实现
# function_name(listname[:])
def print_models(unprinted_designs,completed_models):
	while unprinted_designs:
		current_designs = unprinted_designs.pop()

		print("Printing model： " + current_designs)
		completed_models.append(current_designs)

def print_models_plus(unprinted_designs,completed_models):
	while unprinted_designs:
		current_designs = unprinted_designs.pop()

		print("Printing model： " + current_designs)
		completed_models.append(current_designs)




def show_completed_models(completed_models):
	print("\nThe following models have been printed:")
	for model in completed_models:
		print(completed_models)

unprinted_designs = ['iphone','xiaomi','huawei']
completed_models = []

#print_models(unprinted_designs,completed_models) #这个会让原列表数据清空
print_models_plus(unprinted_designs[:],completed_models)
show_completed_models(unprinted_designs)

