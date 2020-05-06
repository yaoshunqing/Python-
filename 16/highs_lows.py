# encoding= utf-8  
# @Time : 2020/5/6 16:13 
# @Author : Yao
# @File : highs_lows.py 
# @Software: PyCharm
import csv

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

