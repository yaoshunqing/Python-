# encoding= utf-8  
# @Time : 2020/5/6 16:13 
# @Author : Yao
# @File : highs_lows.py 
# @Software: PyCharm
import csv
from matplotlib import pyplot as plt
from datetime import datetime


fig = plt.figure(figsize=(8, 6))


#filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #enumerate获取标题每个元素的索引和值
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    highs, lows, dates = [], [], []
    current_date = 0
    for col in reader:
        #加入错误检查防止存在缺失数据
        try:
            current_date = datetime.strptime(col[0], "%Y-%m-%d")
            high = int(col[1])
            low = int(col[3])
        except:
            print(current_date, 'missing data')
        else:
            lows.append(low)
            dates.append(current_date)
            highs.append(high)

    #plt.plot(list(i for i in range(1,32)), highs, c='red')
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.fill_between(dates, highs, lows,facecolor='blue', alpha=0.1)

    #设置图形格式
    plt.title("Daily high and low temperatures-2014\nDeathValley", fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature(F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=None)
    plt.tight_layout() #放在show前面有作用
    plt.show()


