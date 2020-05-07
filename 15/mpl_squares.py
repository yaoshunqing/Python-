# @Time : 2020/5/5 15:49 
# @Author : Yao
# @File : mpl_squares.py 
# @Software: PyCharm


import matplotlib.pyplot as plt
# 显示中文
# 注意必须在差UN关键画布之前声明
plt.rcParams['font.sans-serif'] = 'SimHei'
# 设置正常显示符号，解决保存图像是符号’-‘显示方块
plt.rcParams['axes.unicode_minus'] = False

# 设置画布尺寸
plt.figure(figsize=(7, 4.8))

# index = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
#
# plt.plot(index, squares, linewidth = 5)
#
# #设置图表标题， 并给坐标轴加上标签
# plt.title("Squares NUmbers", fontsize = 24)
# plt.xlabel("Value", fontsize = 14)
# plt.ylabel("Square of value", fontsize = 14)
#
# #设置刻度标记的大小
# plt.tick_params(axis = 'both', labelsize = 14)

# plt.show()

# #绘制散点图
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
#
# plt.scatter(x_values, y_values, s = 100)
# #设置图表标题， 并给坐标轴加上标签
# plt.title("Squares NUmbers", fontsize = 24)
# plt.xlabel("Value", fontsize = 14)
# plt.ylabel("Square of value", fontsize = 14)
#
# #设置刻度标记的大小
# plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

# plt.show()

# 自动计算数据x轴
x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]
# 删除数据点轮廓edgecolor='none'
# 传递参数c更改数据颜色，当把数据传给c时可以使用camp进行渐变色处理
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
            edgecolor='none', s=40)

# 设置图表标题， 并给坐标轴加上标签
plt.title("哈哈", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

plt.savefig('hh.png')
plt.axis([0, 1100, 0, 1100000])
plt.tight_layout()  # 自动调整大小，让内容都显示在figure内
plt.show()
