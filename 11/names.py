# @Time : 2020/5/2 7:54 
# @Author : Yao
# @File : names.py 
# @Software: PyCharm

from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")

while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\nNeatly formatted name: " + formatted_name + '.')

