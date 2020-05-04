# @Time : 2020/5/1 19:16 
# @Author : Yao
# @File : number_writer.py 
# @Software: PyCharm

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers,f_obj)

def get_stored_username():
    file_name = 'username.json'
    try:
        with open(file_name) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name?")
    file_name = 'username.json'
    with open(file_name, 'w') as f_obj:
        json.dump(file_name,f_obj)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()









