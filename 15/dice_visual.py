# encoding= utf-8  
# @Time : 2020/5/6 15:53 
# @Author : Yao
# @File : dice_visual.py 
# @Software: PyCharm
import pygal
from dice import Dice

#创建一个D6
dice_1 = Dice()
dice_2 = Dice()

#掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides
for value in range(1, max_result + 1):
    #count返回列表中对应值的个数
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')



