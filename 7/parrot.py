# @Time : 2020/4/29 8:16 
# @Author : Yao
# @File : parrot.py 
# @Software: PyCharm

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\n(Enter 'quit' to end the program.)"

# active = True
# while active:
# 	message = input(prompt)
# 	if message == 'quit':
# 		active = False
# 	else:
# 		print(message)


# while 1:
# 	message = input(prompt)
# 	if message == 'quit':
# 		break
# 	else:
# 		print(message)

current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 !=0:
		continue

	print(current_number)


unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)

print("\nThe following users have been confirmed: ")
for i in confirmed_users:
	print(i.title())

pets = ['cat','cat','cat','cat','cat','dog']
print(pets)

#列表去重
print(list(set(pets)))

#删除某list内某重复元素
while'cat' in pets:
	pets.remove('cat')
print(pets)


