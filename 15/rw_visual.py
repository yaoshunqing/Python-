# @Time : 2020/5/6 13:59 
# @Author : Yao
# @File : rw_visual.py 
# @Software: PyCharm

import matplotlib.pyplot as plt
from random_walk import RandomWalk

#设置画布尺寸和让图像及标题内容不会出格
fig = plt.figure(dpi=128, figsize=(6.4, 4.8))
plt.tight_layout()

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:

    #创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(5000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))

    #突出起点和终点
    plt.scatter(0, 0, c='green', edgecolor='none',s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none',s=100)
    plt.scatter(rw.x_values, rw.y_values,  c=point_numbers, cmap=plt.cm.Blues,
                edgecolor='none',s=15)


    # 隐藏边框加坐标轴
    #plt.axis('off')

    # 隐藏坐标轴
    plt.xticks([])  #去掉x轴
    plt.yticks([])  #去掉y轴

    #隐藏坐标轴有报警
    # axes = plt.axes()
    # axes.get_xaxis().set_visible(False)
    # axes.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break