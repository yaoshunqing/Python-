# @Time : 2020/5/1 16:24 
# @Author : Yao
# @File : write_message.py 
# @Software: PyCharm

filename = 'programming.txt'

with open(filename,'w') as file_object:
# 'w'写入模式 'r'读取模式 'a'附加模式 'r+'读取和写入模式
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# 附加模式不会覆盖原有内容
with open(filename,'a') as file_object:
# 'w'写入模式 'r'读取模式 'a'附加模式 'r+'读取和写入模式
    file_object.write("I also love playing.\n")
    file_object.write("I also love playing new games.\n")




