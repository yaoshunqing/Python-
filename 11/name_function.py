# @Time : 2020/5/1 19:45 
# @Author : Yao
# @File : name_function.py 
# @Software: PyCharm

def get_formatted_name(first, last):
    full_name = first + " " + last

    return full_name.title()


print(get_formatted_name('janis','joplin'))