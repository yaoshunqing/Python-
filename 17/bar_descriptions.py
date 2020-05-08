# encoding= utf-8  
# @Time : 2020/5/8 15:05 
# @Author : Yao
# @File : bar_descriptions.py 
# @Software: PyCharm
import pygal
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#336699', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.label_font_size = 14
my_config.title_font_size = 24
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Python Projects on GitHub'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {'value':16101, 'label':'Description of httpie.'},
    {'value':15028, 'label':'Description of django.'},
    {'value':14798, 'label':'Description of flask.'},
]
chart.add('', plot_dicts)
chart.render_to_file('bar_repos.svg')
