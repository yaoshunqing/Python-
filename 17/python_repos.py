# encoding= utf-8  
# @Time : 2020/5/8 10:29 
# @Author : Yao
# @File : python_repos.py 
# @Software: PyCharm
import requests
import pygal
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS, LightenStyle as LS
import json
import requests

# cookies = {
#     '_ga': 'GA1.2.390154780.1563148338',
#     '_octo': 'GH1.1.1062613032.1563148339',
#     'logged_in': 'yes',
#     'dotcom_user': 'yaoshunqing',
# }
#
# headers = {
#     'Connection': 'close',
#     'Pragma': 'no-cache',
#     'Cache-Control': 'no-cache',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'Sec-Fetch-Site': 'none',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-User': '?1',
#     'Sec-Fetch-Dest': 'document',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
# }
#
# params = (
#     ('q', 'language:python'),
#     ('sort', 'stars'),
# )
#
# r = requests.get('https://api.github.com/search/repositories', headers=headers, params=params, cookies=cookies)

#执行API调用并存储响应
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# r = requests.get(url)
# print("Status code: ", r.status_code)
# print(type(r.content))
#将API响应存储在一个json中,再打开
file_name = 'repositories.json'
with open(file_name, 'r',  encoding='UTF-8') as f_obj:
    response_dict = json.load(f_obj)

#response_dict = r.json()
#print("Total repositories:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)
#可视化
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
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')


