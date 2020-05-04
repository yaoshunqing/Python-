# @Time : 2020/5/1 14:36 
# @Author : Yao
# @File : file_reader.py 
# @Software: PyCharm

file_name = 'pi_digits.txt'


with open(file_name) as file_object:
	# contents = file_object.read()
	# print(contents.rstrip())

	lines = file_object.readlines()
	# for line in lines:
	# 	print(line.replace('\n',''))
pi_string = ''
for line in lines:
	pi_string += line.replace('\n','').replace(' ','')

print(pi_string)

file_name_million = 'pi_million_digits.txt'

with open(file_name_million) as file_object:
	# contents = file_object.read()
	# print(contents.rstrip())

	lines = file_object.readlines()
	# for line in lines:
	# 	print(line.replace('\n',''))
pi_string = ''
for line in lines:
	pi_string += line.replace('\n','').replace(' ','')

print(pi_string[:52] + '...')

birthday = input("Enter your birthday, in the form yymmdd: ")
if birthday in pi_string:
	print("You birthday appears in the first million of pi!")
else:
	print("You birthday does not appears in the first million of pi!")


