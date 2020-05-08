# encoding= utf-8  
# @Time : 2020/5/8 10:29 
# @Author : Yao
# @File : python_repos.py 
# @Software: PyCharm
import requests

#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

print("Status code: ", r.status_code)

#将API响应存储在一个变量中
response_dict = r.json()

print(response_dict.keys())


