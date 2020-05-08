# encoding= utf-8  
# @Time : 2020/5/8 9:10 
# @Author : Yao
# @File : americas.py 
# @Software: PyCharm
import pygal
import pygal_maps_world.maps as pwm
wm = pwm.World()
wm.title = 'North, Central, and the America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'zr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
                         'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')

