# @Time : 2020/4/26 7:36 
# @Author : Yao
# @File : bicycle-列表基本处理.py
# @Software: PyCharm

bicycle = ['trek','cannondale','redline','spcialized']

print(bicycle[0])
print(bicycle[-1]) #倒数第一个元素，最后一位
print(bicycle[-2]) #倒数第二个元素


for i in bicycle:
	print('My bike is ' + i.title())

bicycle.append('giant') #末尾添加元素
bicycle.insert(1,'merida') #指定位置插入
del bicycle[3] #永久删除del
poped_bike = bicycle.pop() #删除元素后可以继续使用
bicycle.remove('cannondale') #移除指定名称元素

print(bicycle)
print(poped_bike)

invite = []

print("Please write the 5 VIPs you want to invite: ")
for i in range(0,5):
	invite.append(input())
print(invite)
print("I only can have dinner with 2 of them, so they are: ")

for i in range(4,2,-1):
	invite.pop(i)

print(invite)
