# @Time : 2020/5/1 16:35 
# @Author : Yao
# @File : division.py 
# @Software: PyCharm

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	try:
		#可能引发异常的代码才需要放在try语句中
		answer = int(first_number) / int(second_number)
	except Exception as e:
		#出现异常后怎么办
		print("You can't divide by 0!")
	else:
		#try部分内容成功运行后在执行else
		print(answer)