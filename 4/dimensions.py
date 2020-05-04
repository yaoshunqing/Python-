# @Time : 2020/4/27 9:41 
# @Author : Yao
# @File : dimensions.py 
# @Software: PyCharm

#元组内容不能修改
dimensions = (200,50)
#dimensions[0]= 0 直接就会提示错误
print(dimensions)
#比起列表元组是更简单的数据结构，可以通过复制修改元组内容
dimensions = (499,20)
print(dimensions)




